# Eigensolver

Eigenvalue solver with REST api written in Python3

## Requirements

### Python3 

For Linux:

	$ sudo apt-get install python3

For MacOS

	$ brew install python3

### Python3 Packages

	$ python3 -m pip install -r requirements.txt

## Run

	$ python3 eigensolver.py 8080

## Test

You can use the `test.py` script to generate test request to the solver after you started the server. This script assumes server port `8080`

	$ python3 test.py
