from abc import ABC, abstractmethod
from typing import List

class DocumentLoader(ABC):
    @abstractmethod
    def load_documents(self) -> List:
        pass