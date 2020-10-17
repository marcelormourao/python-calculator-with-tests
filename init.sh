#!/bin/bash

python3 -m venv $(pwd)

source bin/activate

pip3 install -r requirements.txt

export FLASK_APP=controller.py