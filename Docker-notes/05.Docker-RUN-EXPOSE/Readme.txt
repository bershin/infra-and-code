RUN will execute the command and create a new layer on top of the current image.
- invalidate the cache or during the build time.
EXPOSE tell container to listen on certain port

docker build -t nginx-run-expose:v1 .
docker run --name run-expose -p 8080:80 -p 8081:8081 -p 8082:8082 -p 8083:8083 -d nginx-run-expose:v1
docker exec -it run-expose ls -l /usr/share/nginx/html
docker exec -it run-expose ls -l /etc/nginx/conf.d/
docker exec -it run-expose /bin/sh
/ # hostname
/ # curl http://localhost
/ # curl http://localhost:8081