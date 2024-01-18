# Advent of Code 2020

Python solutions to [Advent of Code 2020](https://adventofcode.com/2020)

## Setup

The test package `pytest` is used for running the solutions to the test puzzle cases.
Install it in a virtual environment as follows:

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt 
```

To run solutions you need a folder `real` under the `data` directory that contains puzzle input files.
Create the folder and add puzzle files as follows:

```
data/
└── real/
    ├── day01.txt
    ├── day02.txt
    ├── day03.txt
    └── ...
```

## Run

Run a puzzle solution with

    python src/day01.py

## Test

Run a test puzzle with

    pytest tests/test_day01.py

or run all tests with

    pytest
