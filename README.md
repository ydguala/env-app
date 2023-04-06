# env-api
## Intro
This is a python Flask app that generates a web app that returns a custom message.

It is also used for retrieving the hostname where the app is running and debugging some env vars from the host too.

## How does it work?

This python app requires 3 args.

```
python3 api-server.py "my_app" "USER" "Good Morning"
```

- ARG 1: app name
- ARG 2: host environment variable name
- ARG 3: custom message

It will use the vars to present a message like: app_name, var2 and custom message to print a message like :
```
Hello, World! This is app my_app! I have a var called USER with value ydguala. And I have a message for you: Good Morning
```

## Endpoints
It expose some endpoints that only allow method `GET` for the web app to retrieve some values.

|Endpoint|Method|Description| Example Response |
|---|---|---|---|
|/| GET | Returns the custom message | `<p>Hello, World! This is the app: my_app! I have a var called USER with value ydguala. And I have a message for you: Good Morning</p>`|
|/status | GET | Returns a json with the status, name of the app and the time | `{"app": "APP1", "status": "ok", "time": "2023-04-06T09:18:07"}`|
|/${app_name} | GET | Returns a json with the key 'app_name' and value of ARG 1 | `{"my_app": "APP1"}` |
|${app_name}/api | GET | Returns a json with the key 'api' and value of ARG 1 | `{"api": "APP1"}` |
|/${app_name}/api/message | GET | Returns a json with the key 'message' and value of the message passed as ARG 3 | `{"message": "Good morning"}` |
|/\${app_name}/api/${var2}| GET | Returns a json with the key passed as ARG 2 and value of the host environment variable of this var. If var not found returns 'UNKNOWN' | `{"USER": "ydguala"}` |
|/\${app_name}/api/hostname| GET | Returns a json with the key 'HOSTNAME' and value of the host that is running the Flask app | `{"HOSTNAME": "my_laptop"}` |


## Run as a Container

```
podman run -dt -p 8080:8080 ydoyarzo/env-api:latest APP1 PYTHON_VERSION byebye
```