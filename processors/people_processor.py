import pandas as pd

from processors.entity_processor import EntityProcessor


class PeopleProcessor(EntityProcessor):
    def process(self, json_data: list) -> pd.DataFrame:
        df = pd.DataFrame(json_data)
        # Перейменування поля "name" на "full_name"
        df.rename(columns={'name': 'full_name'}, inplace=True)
        return df
