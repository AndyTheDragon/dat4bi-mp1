import pandas as pd
import json, os

def biread_json(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as data_file:
        data = json.load(data_file)
    return pd.json_normalize(data)
