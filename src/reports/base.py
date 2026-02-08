from abc import ABC, abstractmethod
from typing import Iterable, List
from src.models.record import Record

class BaseReport(ABC):
    @abstractmethod
    def generate(self, records: Iterable[Record]) -> List[List[str]]:
        pass
