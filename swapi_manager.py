import argparse
import json

from swapi_client import SWAPIClient
from swapi_data_manager import SWAPIDataManager


def main():
    # Ініціалізація парсера аргументів
    parser = argparse.ArgumentParser(description="SWAPI Data Manager")
    parser.add_argument("--endpoint", type=str,
                        help="Comma-separated list of entities to fetch (e.g. 'people,planets')", required=True)
    parser.add_argument("--output", type=str, help="Output Excel file name", required=True)
    parser.add_argument("--filters", type=str,
                        help="Filters as JSON string (e.g. '{\"people\": [\"films\", \"species\"]}')", required=False,
                        default='{}')

    args = parser.parse_args()

    # Створюємо клієнт для SWAPI
    client = SWAPIClient(base_url="https://swapi.dev/api/")

    # Створюємо менеджер даних
    manager = SWAPIDataManager(client)

    # Завантажуємо та фільтруємо сутності
    endpoints = args.endpoint.split(',')
    filters = json.loads(args.filters)

    for endpoint in endpoints:
        manager.fetch_entity(endpoint)
        if endpoint in filters:
            manager.apply_filter(endpoint, filters[endpoint])

    # Зберігаємо дані в Excel
    manager.save_to_excel(args.output)


if __name__ == "__main__":
    main()
