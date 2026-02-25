ARG is available only during build time of image.

docker build -t nginx_arg:v1 .
docker run --name nginx-arg -p 8080:80 -d nginx_arg:v1
curl http://localhost:8080
docker exec -it nginx-arg nginx -v

===========Overrite ARG in command line
docker build --build-arg NGINX_VERSION=1.28.1 -t nginx_arg:v2 .
docker run --name nginx-arg2 -p 8081:80 -d nginx_arg:v2
docker exec -it nginx-arg2 nginx -v
curl http://localhost:8081