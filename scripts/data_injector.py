from pathlib import Path
from os import walk
from os.path import basename
import json

collections_src = Path("collections").resolve()
collections_dist = Path("src", "dummyapi-django", "DummyApi").resolve()

if not Path(collections_dist, "api_collections.py").resolve():
    open(Path(collections_dist, "api_collections.py").resolve(), "w").close()

file = open(Path(collections_dist, "api_collections.py").resolve(), "a")


def get_filename(filename, extension=".py"):
    return "".join((filename.split(".")[0], extension))

def join_path(filename):
    return Path(collections_dist, filename).resolve()

for root, dirs, files in walk(collections_src):
    for file_name in files:
        file_path = Path(root, file_name)

        # if not Path(collections_dist, basename(file_path.parent.resolve())).is_file():
        #     open(join_path(get_filename(basename(file_path.resolve()))), "w").close()

        # file_dst = open(join_path(get_filename(basename(file_path.resolve()))), "a")
        json_data = json.load(open(file_path.resolve(), "r"))        

        data = f"{get_filename(basename(file_path).upper(), extension='')} = {json_data}\n"

        file.write(data)

        # file_dst.write(data)

file.close()

