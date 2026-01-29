#!/bin/bash
## Initializes the project's venv

set -eu

project_dir="$(dirname "$0")"
venv="$project_dir/.venv"

# Determine the Python interpreter
if [[ -z "${PYTHON_INTERPRETER:=}" ]]; then
    if [[ -s "$project_dir/python_interpreter" ]]; then
        PYTHON_INTERPRETER="$(cat "$project_dir/python_interpreter")"
    else
        if [[ -z "${PYTHON_VERSION:=}" ]]; then
            if [[ -s "$project_dir/python_version" ]]; then
                PYTHON_VERSION="$(cat "$project_dir/python_version")"
            else
                PYTHON_VERSION=3
            fi
        fi
        PYTHON_INTERPRETER="python$PYTHON_VERSION"
    fi
fi

# Determine the full path to the Python interpreter
if ! python="$(command -v "$PYTHON_INTERPRETER")"; then
    echo "$0: $PYTHON_INTERPRETER: Python interpreter not found" >&2
    exit 1
fi

# Initialize the Python virtual environment
"$python" -m venv "$venv"

# Install packages using PIP
"$venv/bin/pip" install -r "$project_dir/requirements.txt"
