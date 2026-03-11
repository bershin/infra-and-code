?? What is volumes
Persisting data beyond the container's lifecycle.
- Docker volumes enable you to persist data outside the container lifecycle. 
- Volumes act as managed directories or files, seperate from the containers filesystem, ensuring your data remains safe and accessible outside the container as well.

?? Benefits of using volume:
- Data persistence:
    - Persist your data even if the container stops or removed.
- Data Sharing:
    - Share data between multiple containers by sharing the same volume.
- Backup & recovery:
    - Easily backup and restore your valuable data.
- Decoupling data from containers:
    - Gain flexibility in managing and deploying containers by seperating data from application runtime.

?? Type of docker volume
- Bind mounts:
    - Directly link host system directories or files to your containers.
    - Ideal for real time evelopment updates.
- Named volumes:
    - Created by the user and reusable across containers.
    - Best match for perfect for persistent data.
- Anonymous volume:
    - Anonymously created, but without a name that enables reusability.
    - Not often used. Temporray data that doesn't need to persist.

Volume is prefered mechanism for persisting data.
- Completely Managed by Docker.
- Easier to backup and migrate.
- Work on both Linux & Windows.
- Safely shared among multiple containers.
Bind mount are dependent on directory structure and OS of the host machine.

=======Prove data get destroyed when the container destroy
% docker run --name webserver -d -p 8080:80 nginx:1.27.0 
% docker exec -it webserver sh
> echo "hello world" >/usr/share/nginx/html/index.html
> exit
http://localhost:8080 -> "hello world"
% docker stop webserver
% docker start webserver
http://localhost:8080 -> "hello world"

% docker stop webserver
% docker rm webserver
% docker run --name webserver -d nginx:1.27.0 
http://localhost:8080 -> default nginx page

#################################
=======Create named volume 
docker volume create my-vol
=======List all volume 
docker volume ls
=======Get information about a volume like driver mountpoint etc
docker volume inspect my-vol

=======Create anonymous volume 
docker volume create
=======Remove anonymous volume not used
docker volume prune

=======Find volumes not associated with any containers
% docker volume ls -f dangling=true
% docker volume ls -f dangling=true -q
=======Remove all volume not associated with any containers
docker volume prune -a

======Remove any volume specifically
docker volume rm my-vol
###################################

?? Prove volume can be shared across container.
% docker volume create website-data
% docker run --rm -d -p 8081:80 -v website-data:/usr/share/nginx/html nginx:1.27.0
% curl http://localhost:8081
% docker run --rm -d -p 8082:80 -v website-data:/usr/share/nginx/html nginx:1.27.0
% docker run --rm -d -p 8083:80 -v website-data:/usr/share/nginx/html nginx:1.27.0
% curl http://localhost:8082
% curl http://localhost:8083
% docker exec <container_id> sh -c 'echo "Hello from Web1" > /usr/share/nginx/html/index.html'
% curl http://localhost:8081
% curl http://localhost:8082
% curl http://localhost:8083

??
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

$ docker run --name demo-vol7 -p 8087:80 --mount type=bind,source="$(pwd)"/static-files/,target=/usr/share/nginx/html -d vol-img:v1
