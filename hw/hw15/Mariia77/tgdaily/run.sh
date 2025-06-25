#!/bin/bash

cd "$(dirname "$0")/src/tgdaily"

python3 main.py "$@"
