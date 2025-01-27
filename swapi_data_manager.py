import logging
import pandas as pd

from swapi_client import SWAPIClient


# Налаштування логера
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class SWAPIDataManager:
    def __init__(self, client: SWAPIClient):
        """
        Ініціалізація класу для керування завантаженням даних і їх обробкою.

        :param client: екземпляр SWAPIClient
        """
        self.client = client
        self.data = {}

    def fetch_entity(self, endpoint: str):
        """
        Завантажує сутність для вказаного endpoint і зберігає її у DataFrame.

        :param endpoint: endpoint для завантаження даних
        """
        raw_data = self.client.fetch_json(endpoint)
        self.data[endpoint] = pd.DataFrame(raw_data)
        logger.info(f"Fetched {len(raw_data)} records for {endpoint}")

    def apply_filter(self, endpoint: str, columns_to_drop: list):
        """
        Видаляє стовпці з DataFrame для вказаного endpoint.

        :param endpoint: endpoint для обробки
        :param columns_to_drop: список стовпців для видалення
        """
        if endpoint in self.data:
            self.data[endpoint] = self.data[endpoint].drop(columns=columns_to_drop, errors='ignore')
            logger.info(f"Applied filter for {endpoint}, dropped columns: {columns_to_drop}")
        else:
            logger.warning(f"Data for {endpoint} not found.")

    def save_to_excel(self, filename: str):
        """
        Зберігає всі дані у файл Excel.

        :param filename: ім'я файлу для збереження
        """
        with pd.ExcelWriter(filename) as writer:
            for endpoint, df in self.data.items():
                df.to_excel(writer, sheet_name=endpoint.capitalize(), index=False)
                logger.info(f"Saved {endpoint} data to sheet.")
        logger.info(f"Data successfully saved to {filename}.")
