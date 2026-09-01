import json
from pathlib import Path


def load_json_files(folder_path):

    records = []
    folder = Path(folder_path)

    for file in folder.glob("*.json"):
        try:
            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)
                records.append(data)

        except UnicodeDecodeError:
            print(
                f"Skipping {file.name}: encoding problem"
            )

        except json.JSONDecodeError:
            print(
                f"Skipping {file.name}: invalid JSON"
            )

        except Exception as e:
            print(
                f"Skipping {file.name}: {e}"
            )

    return records