#! /bin/bash

chmod +x ./build.sh
./build.sh
git add .
git commit -m 'automated commit'
git push