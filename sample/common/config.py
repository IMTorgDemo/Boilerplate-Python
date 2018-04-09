# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# IMPORTS

# standard lib
import json
import os

# external lib
import path

try:
    workdir = path.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../"))
except NameError: 
    import sys
    workdir = path.Path(os.path.dirname(os.path.abspath(sys.argv[0])))
    

config = json.loads(open( workdir / "config.json" ).read())

config["WORKING"] = workdir
config["FILE_LOAD"] = config["WORKING"] / config["FILE_LOAD"]