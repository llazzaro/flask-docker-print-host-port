# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t print-host-app:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -p 5000:9001 -d print-host-app
```

The application will be accessible at http:127.0.0.1:9001 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:9001`
