# Blogpy

##  Installation

Then create **docker network** and **volumes** as below.

```sh
$ docker volume create blogpy_postgresql
$ docker volume create blogpy_static_volume
$ docker volume create blogpy_files_volume
```
```sh
$ docker network create nginx_network
$ docker network create blogpy_network
```
You need to create .env file in the project root file with default values.
```sh
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
```
Now run django and postgresql with **docker-compose**.
```sh
$ docker-compose up -d
```
Then run nginx container with **docker-compose**.
```sh
$ cd config/nginx/
$ docker-compose up -d
```
You can see blogpy web page on http://localhost, Template and API's are accessable by  docker containers which you can see with below command.
```sh
$ docker ps -a
```
**Output** should be like this.
```sh
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
fc6cc9d6d3d7        nginx_nginx         "nginx -g 'daemon of…"   2 hours ago         Up 2 hours          0.0.0.0:80->80/tcp       nginx
05103904dcb8        ae80efb17475        "gunicorn --chdir bl…"   2 hours ago         Up 2 hours          0.0.0.0:8000->8000/tcp   blogpy
4a183e90a9eb        postgres:10         "docker-entrypoint.s…"   2 hours ago         Up 2 hours          0.0.0.0:5432->5432/tcp   blogpy_postgresql
```
**nginx** container as common web server, **blogpy** container as django application and **blogpy_postgresql** as postgreSQL database container.
