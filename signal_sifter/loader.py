import json
from pathlib import Path


def read_json_file(file_path):
    """
    Try reading a JSON file using multiple encodings.

    Returns:
        Parsed JSON data if successful.

    Raises:
        UnicodeDecodeError:
            If the file cannot be decoded.
        json.JSONDecodeError:
            If the file contains invalid JSON.
    """

    encodings = [
        "utf-8",
        "utf-8-sig",
        "latin-1",
    ]

    last_error = None

    for encoding in encodings:
        try:
            with open(
                file_path,
                "r",
                encoding=encoding,
            ) as file:
                return json.load(file)

        except UnicodeDecodeError as error:
            last_error = error
            continue

    raise last_error


def log_review(review_file, filename, reason):
    """
    Log files that require manual review.
    """

    with open(
        review_file,
        "a",
        encoding="utf-8",
    ) as file:
        file.write(
            f"{filename} | {reason}\n"
        )


def load_json_files(folder_path):
    """
    Load all JSON files from a folder.

    Valid files are returned as records.
    Files that cannot be processed are logged for review.
    """

    records = []

    folder = Path(folder_path)
    review_file = folder.parent / "report" / "review.log"

    review_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    for file in sorted(folder.glob("*.json")):
        try:
            data = read_json_file(file)
            records.append(data)

        except UnicodeDecodeError:
            reason = "Unable to decode file"

            print(
                f"Logged for review: "
                f"{file.name} ({reason})"
            )

            log_review(
                review_file,
                file.name,
                reason,
            )

        except json.JSONDecodeError as error:
            reason = (
                f"Invalid JSON format: "
                f"{error.msg} "
                f"(line {error.lineno}, column {error.colno})"
            )

            print(
                f"Logged for review: "
                f"{file.name} ({reason})"
            )

            log_review(
                review_file,
                file.name,
                reason,
            )

        except Exception as error:
            reason = f"Unexpected error: {error}"

            print(
                f"Logged for review: "
                f"{file.name} ({reason})"
            )

            log_review(
                review_file,
                file.name,
                reason,
            )

    return records