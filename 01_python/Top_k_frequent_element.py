from collections import Counter
from heapq import nlargest

def top_k_frequent(values, k):
    if k <= 0:
        return []
    counts = Counter(values)
    return [item for item, _ in nlargest(k, counts.items(), key=lambda p: p[1])]