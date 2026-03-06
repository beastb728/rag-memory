from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time

from .ingest import ingest_directory
from .embeddings import embed
from .vector_store import add_chunks


class ChangeHandler(FileSystemEventHandler):

    def __init__(self, folder):
        self.folder = folder

    def _should_ignore(self, path):
        name = Path(path).name

        # Ignore temporary/hidden files created by editors
        if name.startswith("."):
            return True

        if "goutputstream" in name:
            return True

        return False

    def _reindex(self):
        print("\nUpdating index...")

        chunks = ingest_directory(self.folder)

        if not chunks:
            print("No chunks found.")
            return

        texts = [c["text"] for c in chunks]

        embeddings = embed(texts)

        add_chunks(chunks, embeddings)

        print(f"Indexed {len(chunks)} chunks.")

    def on_modified(self, event):
        if event.is_directory or self._should_ignore(event.src_path):
            return

        print(f"\nFile modified: {event.src_path}")
        self._reindex()

    def on_created(self, event):
        if event.is_directory or self._should_ignore(event.src_path):
            return

        print(f"\nFile created: {event.src_path}")
        self._reindex()

    def on_deleted(self, event):
        if event.is_directory or self._should_ignore(event.src_path):
            return

        print(f"\nFile deleted: {event.src_path}")
        # deletion handling can be added later

    def on_moved(self, event):
        if event.is_directory or self._should_ignore(event.dest_path):
            return

        print(f"\nFile moved: {event.dest_path}")
        self._reindex()


def watch_folder(folder):

    folder = str(Path(folder).expanduser())

    event_handler = ChangeHandler(folder)
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=True)

    print(f"\nWatching folder: {folder}")
    print("Press Ctrl+C to stop.\n")

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()