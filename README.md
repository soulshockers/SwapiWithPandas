# SWAPI With Pandas

## Install dependencies
```bash
pip install -r requirements.txt
```

## Online method
```bash
python swapi_manager.py --input https://swapi.dev/api/ --endpoint people,planets --output swapi_data.xlsx
```

## Offline method
```bash
python swapi_manager.py --input swapi_data.xlsx --endpoint people,planets --output result.xlsx
```