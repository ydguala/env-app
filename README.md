# env-api
## Intro
This is a python Flask app that generates a web app that returns a json with keys as the name of the environment variables passed to the script, and the values of the env variables.

## How does it work?

```bash
python3 api-server.py "my_app" "USER" "HOSTNAME"
```

It will use the vars to create the json :
```json
{
  "HOSTNAME": "myMachine",
  "USER": "ydguala",
  "my_app": "aplication1"
}
```

It also exposes the endpoint `/status` which reports a json object like:
```json
{
  "status": "ok",
  "time": "2023-04-07T22:59:05"
}
```


## Run as a Container

```
podman run -dt -p 8080:8080 ydguala/env-api:latest "my_app" "USER" "HOSTNAME"
```