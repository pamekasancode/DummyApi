#!/bin/bash

# echo "$(dirname "$0")"

src="./src/django"
dist=(./tests/django/lib/*[0]/site-packages)


cp -rT $src "$dist/dummyApi"
cp -rT collections "$dist/dummyApi/collections"