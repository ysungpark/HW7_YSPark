import numpy as np

def cos_similarity():
    Docs = np.array([[1, 1, 0, 1, 0, 1],
                     [1, 1, 1, 0, 1, 0],
                     [1, 1, 0, 1, 0, 0]])
    Query = np.array([1, 1, 0, 0, 1, 0])

    dot_product = np.dot(Docs, Query)
    docs_norm = np.linalg.norm(Docs, axis=1)
    query_norm = np.linalg.norm(Query)
    cosine_similarities = dot_product / (docs_norm * query_norm)

    for i, similarity in enumerate(cosine_similarities):
        print(f"doc{i+1} = {similarity:.2f}")

if __name__ == "__main__":
    cos_similarity()
