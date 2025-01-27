import requests
import logging

# Налаштування логера
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class SWAPIClient:
    def __init__(self, base_url: str):
        """
        Ініціалізація з базовою URL-адресою для API.
        """
        self.base_url = base_url

    def fetch_json(self, endpoint: str) -> list:
        """
        Завантажує всі сторінки JSON для вказаного endpoint.

        :param endpoint: endpoint для отримання даних (наприклад, "people")
        :return: список всіх сутностей у вигляді JSON
        """
        all_data = []
        url = f"{self.base_url}{endpoint}/"  # Починаємо з першої сторінки

        while url:
            # Логуємо URL запиту
            logger.info(f"Fetching data from: {url}")

            # Завантажуємо дані з API
            response = requests.get(url)
            response.raise_for_status()  # Викликає помилку, якщо статус код відповіді неправильний
            data = response.json()

            # Додаємо результати до списку
            all_data.extend(data['results'])

            # Переходимо до наступної сторінки
            url = data.get('next')

        return all_data
