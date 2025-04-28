import os
from typing import List
from llama_index.core import SimpleDirectoryReader
from src.core.interfaces.document_loader import DocumentLoader

class SimpleDirectoryLoader(DocumentLoader):
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def load_documents(self) -> List:
        if not os.path.exists(self.directory_path) or len(os.listdir(self.directory_path)) == 0:
            raise FileNotFoundError(f"Document directory '{self.directory_path}' does not exist or is empty!")
        reader = SimpleDirectoryReader(self.directory_path)
        return reader.load_data()
