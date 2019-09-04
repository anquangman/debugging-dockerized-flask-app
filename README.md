# debugging-dockerized-flask-app
Sample code for demonstrate how to debug an dockerized flask application

# Require
1. Docker version 19.03.1
2. Docker-Compose 1.24.1

# How to use
1. Clone
2. Navigate to root directory
3. run ```docker-compose up -d --build```
4. Set checkpoint (e.g at line 15 in app.py)
5. Add config to VSCode launch.json and click start
5. Open your browser and visit http://0.0.0.:5000/. It should stop at your checkpoints.

## launch.json
```
{
    "version": "0.2.0",
    "configurations": [
        ...
        {
            "name":"Attach Debug",
            "type":"python",
            "request":"attach",
            "port":4000,
            "host":"0.0.0.0",
            "pathMappings":[{
                "localRoot":"path to where the app.py lives on your local",
                "remoteRoot":"/usr/src"
            }]
        },
        ...
    ]
}
```
