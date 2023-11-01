import json
from pathlib import Path

JSON_BASE_DIR = Path(Path(__file__).parent.parent.resolve(), "collections")

def parse_from_json(name):
    try:
        file_handler = json.load(open(Path(JSON_BASE_DIR, name), "rb"))

        if not file_handler:
            raise FileNotFoundError(f"Api type with {name} doesn't exists, you can extend your own api data")

    except json.JSONDecodeError:
        print(f"Failed to load {name} data")
        return


    return file_handler




