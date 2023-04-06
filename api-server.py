#!/usr/bin/python3

# IMPORTS

import json
import os
import sys
from datetime import datetime
from flask import *





# FUNCTIONS

# This function will get the first 3 args and set them in order to app_name,var2 and message
def set_args_as_vars():
    help_message = """
    This app will take first 3 args as env var names that will be used as: app_name, var2 and message to print a message like : '<p>Hello, World {app_name}! {var2} = {var2_value}, message: {message}</p>'
    """

    if len(sys.argv) < 3:
        raise Exception('-------- ERROR - need 3 args. {}'.format(help_message))
    else:
        global app_name
        global var2
        global message

        app_name = str(sys.argv[1])
        var2 = str(sys.argv[2])
        message = str(sys.argv[3])


def get_env_var_value(var):
    try:
        env_var = os.environ[var]
    except KeyError:
        print("{} not found".format(var))
        env_var = "UNKNOWN"

    if var == 'HOSTNAME':
            env_var = os.uname()[1]


    return env_var

# GLOBAL VARS
server_port         = 8080
server_host         = "0.0.0.0"
api_server          = Flask('api-server')

# needed to set next vars
set_args_as_vars()

app_name_value = get_env_var_value(app_name)
var2_value = get_env_var_value(var2)


# FLASK FUNCTIONS, needed to be defined after params

@api_server.route('/', methods=['GET'])
def  root():


    return '<p>Hello, World! This is the app: {}! I have a var called {} with value {}. And I have a message for you: {}</p>'.format(app_name, var2,var2_value, message)


@api_server.route('/status', methods=['GET'])
def  status():

    response = {'app' : app_name_value , 'status' : 'ok', 'time' : datetime.now().strftime("%Y-%m-%dT%H:%M:%S") }
    json_response = json.dumps(response)

    return json_response

@api_server.route('/{}'.format(app_name_value), methods=['GET'], strict_slashes=False)
def app():
    response = { app_name : app_name_value }

    json_response = json.dumps(response)

    return json_response

@api_server.route('/{}/api'.format(app_name_value), methods=['GET'], strict_slashes=False)
def api():
    response = { 'api' : app_name_value  }

    json_response = json.dumps(response)

    return json_response

@api_server.route('/{}/api/message'.format(app_name_value), methods=['GET'], strict_slashes=False)
def api_message():
    response = { 'message' : message  }

    json_response = json.dumps(response)

    return json_response

@api_server.route('/{}/api/{}'.format(app_name_value, var2), methods=['GET'], strict_slashes=False)
def api_custom_var():

    response = { var2 : var2_value }

    json_response = json.dumps(response)

    return json_response


@api_server.route('/{}/api/hostname'.format(app_name_value), methods=['GET'], strict_slashes=False)
def api_hostname():

    try:
        hostname = os.uname()[1]
    except KeyError:
        print("{} not found".format(var))
        hostname = "UNKNOWN"

    response = { 'HOSTNAME' : hostname }

    json_response = json.dumps(response)

    return json_response



def main():

    print("app_name arg {} - value {}\nvar2 arg {} - value {}\nmessage arg: {}".format(app_name, app_name_value, var2, var2_value, message))

    api_server.run(host=server_host,port=server_port)

# EXECUTION
if __name__ == "__main__":
    main()