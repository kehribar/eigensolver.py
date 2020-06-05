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

## Operation

Receives POST request to `/eig` endpoint with the following format:

	{"data": [0, 1, 2, 3, 4, 5, 6, 7, 8]}

Converts the input data into numpy array:

	[0 1 2 3 4 5 6 7 8]

Reformats it as 2D array with the following format:

	[[0 3 6]
	 [1 4 7]
	 [2 5 8]]

Then, calculates the eigenvalues of the matrix and returns the following result in the response body:

	13.348469228349522 -1.3484692283495336 -9.991844527712246e-16
