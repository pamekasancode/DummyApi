#!/bin/bash

# echo "$(dirname "$0")"

src="./src/dummyapi-django"
dist=(./tests/django-test/lib/*[0]/site-packages)



cp -rT $src "$dist/dummyapi"
# cp -rT collections "$dist/dummyApi/collections"

# echo "Injecting collections to python file.."

# directory="collections"
# dist=""

# if [ ! -d "$directory" ]; then
#     exit 1
# fi


# for dir in "$directory"/*; do
#     if [ -d "$dir" ]; then
#         echo "$dir"
#         for file in $dir/*; do
#             if [ -f "$file" ]; then
#                 echo "file"
#             fi
#         done
#     fi
# done
