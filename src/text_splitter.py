from document_loader import load_documents


documents = load_documents()

all_chunks = []


for document in documents:

    # Each blank-line-separated item becomes one chunk
    chunks = document["content"].split("\n\n")

    for chunk in chunks:

        chunk = chunk.strip()

        if chunk:
            all_chunks.append({
                "source": document["source"],
                "content": chunk
            })


print(f"Total chunks created: {len(all_chunks)}")

for i, chunk in enumerate(all_chunks):

    print(f"\n--- Chunk {i + 1} ({chunk['source']}) ---")
    print(chunk["content"])