#!/usr/bin/env python
#from . import app
from app import app
import os
  # needed for Heroku:
  # check if a port is defined in an env varibale (e.g. by Heroku)
  # otherwise set to 5000 (local host)
  # define the host is also needed
myPort = int(os.environ.get("PORT", 5000))
if __name__ == '__main__':
    app.run(debug=True, port=myPort)
