import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from text_splitter import all_chunks


model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    local_files_only=True
)

texts = [chunk["content"] for chunk in all_chunks]

embeddings = model.encode(texts)
embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


def retrieve(query, k=6):

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for index_number in indices[0]:
        results.append(all_chunks[index_number])

    return results


if __name__ == "__main__":

    query = input("Ask your question: ")

    results = retrieve(query)

    print("\nRelevant Evidence:\n")

    for result in results:

        print("Source:", result["source"])
        print(result["content"])
        print()