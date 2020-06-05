# -----------------------------------------------------------------------------
# 
# 
# -----------------------------------------------------------------------------
import json
import requests

data = [0, 1, 2, 3, 4, 5, 6, 7, 8]

cmd = {'data': data}
cmd = json.dumps(cmd)

# ...
print("Command: %s" % cmd)

# ...
res = requests.post(
  'http://localhost:8080/eig', 
  json=cmd
)

# ...
print("Response: %s" % res.text)
