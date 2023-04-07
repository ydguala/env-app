#!/usr/bin/python3

# IMPORTS

import json
import os
import sys
from datetime import datetime
from flask import *


# FUNCTIONS
# These functions will get the first 3 args and set them in order to app_name,var2 and message
def set_args_as_vars():

    var_list = []
    for v in sys.argv[1:]:
        var_list.append(v)
    return var_list

def get_env_var_value(var):

    if var == 'HOSTNAME':
        try:
            env_var = os.uname()[1]
        except KeyError:
            env_var = "UNKNOWN"
            print("{} not found".format(var))
    else:
        try:
            env_var = os.environ[var]
        except KeyError:
            env_var = "UNKNOWN"


    return env_var

def create_variables_dictionary(variables_list):

    vars_dict = {}
    for var in variables_list:
        vars_dict[var] = get_env_var_value(var)

    print(str(vars_dict))
    return vars_dict

# GLOBAL VARS
server_port         = 8080
server_host         = "0.0.0.0"
api_server          = Flask('api-server')

# needed to set next vars
global variables_list
global variables_dict
variables_list = set_args_as_vars()
variables_dict = create_variables_dictionary(variables_list)

# FLASK FUNCTIONS, needed to be defined after params

@api_server.route('/', methods=['GET'])
def  root():
    json_response = json.dumps(variables_dict)
    return json_response


@api_server.route('/status', methods=['GET'], strict_slashes=False)
def  status():

    response = {'status' : 'ok', 'time' : datetime.now().strftime("%Y-%m-%dT%H:%M:%S") }
    json_response = json.dumps(response)

    return json_response


def main():
    api_server.run(host=server_host,port=server_port)

# EXECUTION
if __name__ == "__main__":
    main()