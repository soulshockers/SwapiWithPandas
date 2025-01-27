from abc import ABC, abstractmethod
import pandas as pd

class EntityProcessor(ABC):
    @abstractmethod
    def process(self, json_data: list) -> pd.DataFrame:
        """Абстрактний метод для обробки даних."""
        pass
