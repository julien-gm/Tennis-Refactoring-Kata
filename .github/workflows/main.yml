name: Unit tests and formating

on:
  pull_request:
    branches:
      - main

jobs:
  linter:
    runs-on:
      - ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Check formating with flake8
        run: |
          echo "Test Flake8"
          pip install -r requirements.txt
          python -m flake8 *.py
  tests:
    runs-on:
      - ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Run TU
        run: |
          pip install -r requirements.txt
          python -m pytest *test.py
