import pandas as pd

from logger_config import logger
from processors.entity_processor import EntityProcessor

class PeopleProcessor(EntityProcessor):
    def process(self, json_data: list) -> pd.DataFrame:
        # Логування початку процесу
        logger.info("Starting to process 'people' data")

        df = pd.DataFrame(json_data)

        # Перейменування поля "name" на "full_name"
        df.rename(columns={'name': 'full_name'}, inplace=True)

        # Логування завершення процесу
        logger.info("Processing completed for 'people' data")

        return df
