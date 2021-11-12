# Blogpy

##  Installation

1. create **docker network** and **volumes** as below.

```sh
$ docker volume create blogpy_postgresql
$ docker volume create blogpy_static_volume
$ docker volume create blogpy_files_volume
```
```sh
$ docker network create nginx_network
$ docker network create blogpy_network
```
2. Now run django and postgresql with **docker-compose**.
```sh
$ docker-compose up -d
```
3. Create self-sign certificate using OpenSSL.(public key && private key --> .crt && .key files needed):

https://imagineer.in/blog/https-on-localhost-with-nginx/
```
$ openssl req -x509 -sha256 -nodes -newkey rsa:2048 -days 365 -keyout localhost.key -out localhost.crt
```
4. Then run nginx container with **docker-compose**.
```sh
$ cd config/nginx/
$ docker-compose up -d
```
5. You can see blogpy web page on http://localhost, Template and API's are accessable by  docker containers which you can see with below command.
```sh
$ docker ps -a
```
6. **Output** should be like this.
```sh
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
fc6cc9d6d3d7        nginx_nginx         "nginx -g 'daemon of…"   2 hours ago         Up 2 hours          0.0.0.0:80->80/tcp       nginx
05103904dcb8        ae80efb17475        "gunicorn --chdir bl…"   2 hours ago         Up 2 hours          0.0.0.0:8000->8000/tcp   blogpy
4a183e90a9eb        postgres:10         "docker-entrypoint.s…"   2 hours ago         Up 2 hours          0.0.0.0:5432->5432/tcp   blogpy_postgresql
```
**nginx** container as common web server, **blogpy** container as django application and **blogpy_postgresql** as postgreSQL database container.

7. Outputs in browser:
openssl verified by localhost so it is not trusted CA for browser.

![Screenshot from 2021-11-13 00-17-40](https://user-images.githubusercontent.com/45814367/141532535-bb7ea729-ab25-4b91-b075-f8221b513334.png)


8. **usefull command for working with docker:**
```
sudo docker stop container_name
sudo docker rm container_name
sudo docker-compose build
sudo docker ps -a
```
