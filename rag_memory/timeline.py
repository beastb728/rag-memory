from .vector_store import collection
from collections import defaultdict


def show_timeline():
    results = collection.get()

    metas = results["metadatas"]

    timeline = defaultdict(set)

    for meta in metas:
        date = meta["modified"].split("T")[0]
        timeline[date].add(meta["source"])

    for date in sorted(timeline.keys(), reverse=True):
        print("\n" + date)
        for file in timeline[date]:
            print("   ", file)