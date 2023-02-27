#! /bin/bash

pipenv run build

git add .
git commit -m 'automated commit'
git push