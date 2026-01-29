#!/bin/bash

set -eu

project_dir="$(dirname "$0")"
venv="$project_dir/.venv"

if [[ -z "${PYTHONPATH:-}" ]]; then
    export PYTHONPATH="$project_dir"
else
    export PYTHONPATH="$project_dir:$PYTHONPATH"
fi

exec "$venv/bin/python3" -m vety
