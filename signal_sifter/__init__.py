import json
from pathlib import Path


def load_json_files(folder_path):

    records = []

    folder = Path(folder_path)

    for file in folder.glob("*.json"):

        with open(file, "r", encoding="utf-8") as f:

            data = json.load(f)

            records.append(data)

    return records