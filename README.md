# envoy-proxy-websocket
envoy proxy websocket example

## Step 1: Docker Machine setup

```sh
$ docker-machine create --driver virtualbox default
$ eval $(docker-machine env default)
```

## Step 2: Clone the Envoy repo

If you have not cloned the envoy repo, clone it with git clone `git@github.com:envoyproxy/envoy` or git clone `https://github.com/envoyproxy/envoy.git`

## Step 3: clone this repo
clone this repo and move it to `envoy/examples/front-proxy` directory of envoy.

## Step 4: start all of our containers

```shell
$ cd envoy/examples/front-proxy/envoy-proxy-websocket
$ docker-compose up --build -d
$ docker-compose ps
```

once you run `docker-compose ps` command you will see 5v containers running service1, service2, service3, service4 and front-proxy.  service1, service2, service3, service4 have only 80 port exposed and front-proxy will have 80, 8001. 80 port of front proxy is mapped to 80 port of docker machine and 8001 is mapped to 8001 port of docker machine so that using docker machine ip you can access entire `envoymesh`.

## Step 5: Run HTTP route (flask service)

ssh to container service4 and start flask service


```shell
$ docker-compose exec service4 /bin/bash
bash# cd /code
bash# python3 flask_service.py &
bash# exit
```


## Step 6: Test HTTP route

```shell
$ curl -v $(docker-machine ip default):8000/httpservice
```

## Step 7: Test websocket route

```shell
$ cd container_services/
$ python tornado-client.py $(docker-machine ip default):80/service1
```

similarly, test all the routes

```shell
$ python tornado-client.py $(docker-machine ip default):80/service2
```

```shell
$ python tornado-client.py $(docker-machine ip default):80/service3
```

```shell
$ python tornado-client.py $(docker-machine ip default):80/service4
```
