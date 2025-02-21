import pandas as pd

from logger_config import logger
from processors.entity_processor import EntityProcessor

class PeopleProcessor(EntityProcessor):
    def process(self, json_data: list) -> pd.DataFrame:
        # Логування початку процесу
        logger.info("Starting to process 'people' data")

        df = pd.DataFrame(json_data)

        # Видалення стовпця "films", якщо він існує
        df.drop(columns=['films'], errors='ignore', inplace=True)

        # Логування завершення процесу
        logger.info("Processing completed for 'people' data")

        return df