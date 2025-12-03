#!/bin/bash

project_dir="$(dirname "$0")"
venv="$project_dir/venv"

"$venv/bin/python3" -m vety
