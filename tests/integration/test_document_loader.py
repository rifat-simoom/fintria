from src.core.services.simple_directory_loader import SimpleDirectoryLoader

def test_load_documents_success(tmp_path):
    # Create a fake document
    d = tmp_path / "banking_docs"
    d.mkdir()
    file = d / "doc1.txt"
    file.write_text("Sample banking document content.")

    loader = SimpleDirectoryLoader(directory_path=str(d))
    documents = loader.load_documents()
    assert len(documents) == 1
