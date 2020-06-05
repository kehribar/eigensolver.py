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

  print("")
  print("Input:")
  print(inp)

  print("")
  print("Diagonalised:")
  print(np.diag(inp))

  [v, d] = np.linalg.eig(np.diag(inp))
  
  print("")
  print("v:")
  print(v)

  print("")
  print("d:")
  print(v)

  print("")

  retval = json.dumps({"return": v.tolist()})
  return retval

# ...
try:
  app.logger.disabled = True
  app.run(host='localhost', port=PORTNUM)  
except:
  sys.exit(-1)

# ...
sys.exit(0)
