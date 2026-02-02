Volume is prefered mechanism for persisting data.
- Completely Managed by Docker.
- Easier to backup and migrate.
- Work on both Linux & Windows.
- Safely shared among multiple containers.
Bind mount are dependent on directory structure and OS of the host machine.

=======Create named volume 
docker volume create my-vol
docker volume ls
docker volume inspect my-vol
=======Create anonymous volume 
docker volume create

=======Remove anonymous volume not used
docker volume prune
=======Remove all volume not used
docker volume prune -a
======Remove any volume specifically
docker volume rm my-vol


docker run --name my-nginx-vol -p 8080:80 --mount type=volume,source=vol101,target=/myapp1 -d nginx:alpine-slim
docker run --name=nginx-vol2-doc -p 8082:80 -v vol102:/myapp2 -d nginx:alpine-slim
docker ps
docker exec -it my-nginx-vol /bin/sh
df -h
echo "Hello there" > /myapp1/file1.txt
exit

docker volume ls
docker volume inspect vol101
sudo ls -l /var/lib/docker/volumes/vol101/_data
docker volume rm vol101 vol102


# Check the website is loading
docker run --name demo-vol2 -p 8082:80 -d vol-img:v1 
# Copy the content to volume
docker run --name demo-vol1 -p 8081:80 --mount type=volume,source=myvol1,target=/usr/share/nginx/html -d vol-img:v1
# Mount the content from volume.
docker run --name demo-vol2 -p 8082:80 -v myvol1:/usr/share/nginx/html -d nginx:alpine-slim
$ docker exec -it demo-vol2  /bin/sh
/ # df -h
# echo "write mode" >test.html
exit
$ curl http://localhost:8082/test.html

Readonly mount:
docker run --name demo-vol3 -p 8083:80 --mount type=volume,source=myvol1,target=/usr/share
/nginx/html,readonly -d vol-img:v1
docker exec -it demo-vol3  /bin/sh
df -h
cd /usr/share/nginx/html
cp index.html app1/backup.html # readonly
exit

docker run --name demo-vol4 -p 8084:80 -v myvol1:/usr/share/nginx/html:ro -d nginx:alpine-
slim
docker exec -it demo-vol4  /bin/sh
df -h
cd /usr/share/nginx/html
cp index.html app1/backup.html # readonly
exit

docker run --name demo-vol6 -p 8086:80 --mount type=volume,source=myvol1,target=/usr/share
/nginx/html/app1,volume-subpath=app1 -d vol-img:v1
docker exec -it demo-vol6  /bin/sh

$ docker run --name demo-vol7 -p 8087:80 --mount type=bind,source="$(pwd)"/static-files/,tar
get=/usr/share/nginx/html -d vol-img:v1
