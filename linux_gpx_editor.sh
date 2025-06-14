#!/bin/bash
echo "Satrt GPX Editor"
if [" -d "./venv"]; then
    echo"install virtual python enviroment"
    python3 -m venv ./venv
fi
echo "instalation finished"
source ./venv/bin/activate
echo "install seit-package"
pip install -r requirements.txt
python3 main.py
$SHELL