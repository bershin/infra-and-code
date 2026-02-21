Capital 'P' map random host port to the ports exposed in container.

docker build -t port:v2 .
docker run --name port-2 -P -d port:v2
# fetch the host port
docker ps 

curl http://localhost:<random-port>