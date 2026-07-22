import numpy as np

def nearest(query: np.ndarray, matrix: np.ndarray, k: int) -> np.ndarray:
    query = query / max(np.linalg.norm(query), 1e-12)
    scores = matrix @ query
    
    k = min(k, len(scores))  
    idx = np.argpartition(-scores, k - 1)[:k]
    return idx[np.argsort(-scores[idx])]


query = np.array([1, 0])
matrix = np.array([
    [1, 0],
    [0.8, 0.6],
    [0, 1],
    [-1, 0]
])
k = 2

result = nearest(query, matrix, k)
print(result)