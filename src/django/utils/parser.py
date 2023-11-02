import json
from pathlib import Path

JSON_BASE_DIR = Path(Path(__file__).parent.parent.resolve(), "collections")

def parse_from_json(*paths):
    try:
        file_handler = json.load(open(Path(JSON_BASE_DIR, *paths), "rb"))

        if not file_handler:
            raise FileNotFoundError(f"Api type with {Path(*paths)} doesn't exists, you can extend your own api data")

    except json.JSONDecodeError:
        print(f"Failed to load {Path(*paths)} data")
        return


    return file_handler




