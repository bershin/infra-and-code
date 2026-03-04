# Install vim via dockerfile
docker build -t web_server .
docker images
docker run -d web_server
docker ps
docker exec -it <cid> sh
-> vim
-> exit
docker stop <cid>
docker rm <cid>
