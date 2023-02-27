#! /bin/bash
python3 -m pipenv run pip freeze > requirements.txt
python3 -m pipenv run pip install --requirement requirements.txt
zip -r scribble-ai.zip . -x "*.git*" "*.venv*" "*.vscode*" "*.idea*" "*.DS_Store*"