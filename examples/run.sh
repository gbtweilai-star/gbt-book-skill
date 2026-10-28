#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_book_skill info
PYTHONPATH=src python -m gbt_book_skill check --payload '{}'
PYTHONPATH=src python -m gbt_book_skill run   --payload '{}'
