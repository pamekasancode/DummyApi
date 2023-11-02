import requests
import json
from pathlib import Path
from os.path import isfile, isdir
from os import mkdir


BASE_PATH = Path(__file__).parent.parent.resolve()



def dump_json(title, data):
    file_path = Path(BASE_PATH, "collections", title).resolve()

    if isfile(file_path):
        raise FileExistsError(f"File with {title} name is already exists")

    
    json.dump(data, open(file_path, 'w'))




def get_json_placeholder():
    API_DATA_CATAGORIES = ['posts', 'comments', 'albums', 'photos', 'todos', 'users']

    if not isdir(Path(BASE_PATH, "collections", "json_placeholder")):
        mkdir(Path(BASE_PATH, "collections", "json_placeholder"))


    for path in API_DATA_CATAGORIES:
        res = requests.get(f"https://jsonplaceholder.typicode.com/{path}")

        dump_json(Path("json_placeholder", f"{path}.json"), res.json())

    print("All data has been saved")


def get_custom_api(url):
    data = requests.get(url).json()

    if not data:
        raise Exception(f"Data is empty got {data}")

    dump_json("", data)



get_json_placeholder()
