#!/usr/bin/python3

# IMPORTS

import json
import os
import sys
from datetime import datetime
from flask import *


# GLOBAL VARS
server_port         = 8080
server_host         = "0.0.0.0"
api_server          = Flask('api-server')


# FUNCTIONS

@api_server.route('/', methods=['GET'])
def  home():

    response = {'status' : 'ok', 'message' : 'home', 'time' : datetime.now().strftime("%Y-%m-%dT%H:%M:%S") }
    json_response = json.dumps(response)

    return json_response

@api_server.route('/env', methods=['GET'])
def  env():

    response = {'env' : dict(os.environ)  }
    json_response = json.dumps(response)

    return json_response

@api_server.route('/hostname', methods=['GET'])
def  hostname():

    # get hostname
    try:
        hostname = os.uname()[1]
    except KeyError as e:
        print("hostname not found {}".format(e))
        hostname = "UNKNOWN"

    # get namespace
    try:
        ns = os.environ['NAMESPACE']
    except KeyError as e:
        print("namespace not found {}".format(e))
        ns = "UNKNOWN"

    response = { 'HOSTNAME' : hostname , 'NAMESPACE' : ns }

    json_response = json.dumps(response)

    print("\n ==========> /hostname : {} , namespace : {}\n".format(hostname,ns))

    return json_response



def main():

    api_server.run(host=server_host,port=server_port)


# EXECUTION
if __name__ == "__main__":
    main()