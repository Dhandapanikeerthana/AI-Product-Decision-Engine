from pathlib import Path


DATA_FOLDER = Path("data")


def load_documents():
    documents = []

    for file_path in DATA_FOLDER.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": file_path.name,
            "content": content
        })

    return documents


if __name__ == "__main__":
    documents = load_documents()

    for document in documents:
        print(f"\n--- {document['source']} ---")
        print(document["content"])