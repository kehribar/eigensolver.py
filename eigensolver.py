# -----------------------------------------------------------------------------
# 
# 
# -----------------------------------------------------------------------------
import sys
import json
import numpy as np
from flask import Flask
from flask import request

# ...
DEBUG = False

# ...
if((len(sys.argv) < 2)):
  print("Missing arguments!")
  print("Usage: python3 eigensolver.py PORTNUM")
  sys.exit(-1)
if(((sys.argv[1]).isnumeric()) == False):
  print("Invalid argument for port number: %s" % (sys.argv[1]))
  print("Usage: python3 eigensolver.py PORTNUM")
  sys.exit(-1)

# ...
PORTNUM = int(sys.argv[1])

# ...
app = Flask(__name__)

# ...
@app.route('/')
def homepage():
  return "eigensolver.py is running"

# ...
@app.route('/eig', methods=['POST'])
def eigensolver():
  inp = json.loads(request.json)
  inp = inp['data']
  inp = np.asarray(inp)
  inp_size = len(inp)

  # ...
  dimsize = int(np.sqrt(len(inp)))

  # ...
  if(DEBUG):
    print("")
    print("Input:")
    print(inp)

  # ...
  inp = np.resize(inp, (dimsize, dimsize))
  inp = np.transpose(inp)

  # ...
  if(DEBUG):
    print("")
    print("Reformatted:")
    print(inp)

  # Run the solver
  d, v = np.linalg.eig(inp)
  
  # ...
  if(DEBUG):
    print("")
    print("v:")
    print(v)
    print("")
    print("d:")
    print(d)
    print("")

  # ...
  v = np.resize(v, (1, inp_size))

  # ...
  if(DEBUG):
    print("Reformatted result:")
    print(v)
    print("")

  # ...
  return np.array_str(v).strip('[]')

# ...
try:
  app.logger.disabled = True
  app.run(host='localhost', port=PORTNUM)  
except:
  sys.exit(-1)

# ...
sys.exit(0)
