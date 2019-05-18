#!/usr/bin/env bash

set -ex # fail on first error, print commands

command -v conda >/dev/null 2>&1 || {
  echo "Requires conda but it is not installed.  Run install_miniconda.sh." >&2;
  exit 1;
}

# Install tutorial dependencies
pip install --upgrade pip


#  Install editable using the setup.py
pip install  --no-cache-dir -r requirements.txt
