####################### Docker command ########################

==============Spin a docker container
# Run from dockerhub base image
docker run --name <name_of_container> -p <host_port:<container_port> -d <image_name>
docker run --name my-nginx -p 8080:80 -d nginx
 - curl http://localhost:8080
# From local custom image
docker run --name my-first-custom-container -p 8081:80 -d my-first-nginx-custom-image:v1
# From dockerhub custom image
docker run --name nginx-container-2 -p 8082:80 -d 230882/my-first-nginx-custom-image:v2
# pass environment variable
docker run --name cmd-env-dev -p 5002:5000 -e APP_ENVIRONMENT=dev -d env-cmd:v2
# overrite CMD or append entrypoint
docker run --name ep-3 entrypoint:v1 "bershin"
# Overrite entrypoint
docker run --name ep-4 --entrypoint "/bin/sh" entrypoint:v1 -c "echo BUILD YOUR DREAM"
# Docker to decide a random host port
docker run --name nginx-container-2 -p 80 -d 230882/my-first-nginx-custom-image:v2
# Docker fetch exposed container port and decide a random host port
docker run --name nginx-container-2 -P-d 230882/my-first-nginx-custom-image:v2
# Docker run with vollume, volumes & mount are automaticaly created.
docker run --name my-nginx-vol -p 8080:80 --mount type=volume,source=vol101,target=/myapp1 -d nginx:alpine-slim
docker run --name=nginx-vol2-doc -p 8082:80 -v vol102:/myapp2 -d nginx:alpine-slim

=================Build a docker image
docker build -t my-first-nginx-custom-image:v1 .
docker build --build-arg NGINX_VERSION=1.28.1 -t nginx_arg:v2 .
docker build --no-cache -t nginx-run-expose:v2 .

=================tag & push image
docker tag my-first-nginx-custom-image:v1 230882/my-first-nginx-custom-image:v1
docker push 230882/my-first-nginx-custom-image:v2 
##Require docker login## -> docker login

================Verify docker containers & images
# Only running
docker ps
# Running and stopped
docker ps -a
docker ps --format "table {{.Image}}\t{{.Ports}}"
# Check the image build status
docker images

===============Stop a docker container
docker stop <container_name>
docker stop my-nginx

===============Remove a docker container & images
# Remove Stopped container
docker rm <container_name>
docker rm my-nginx
# Remove running container with out stopping
docker rm -f <container_name>
docker rm -f my-nginx
# Stop and remove all container
docker rm -f $(docker ps -aq)

# Remove image
docker rmi <image>
# Remove all images
docker rmi -f $(docker images -q)
==============Execute command in container
# Without login
docker exec -it nginx-container-2  ls /usr/share/nginx/html/
# After login
docker exec -it nginx-container-2 /bin/bash
# Login as root user
docker exec --user root -it cont-40 /bin/bash

============Search image in docker hub using command
docker search nginx
docker search nginx --limit 5
docker search nginx --filter=stars=50
docker search nginx --filter=is-official=true

==============Inspect images & containers
#images:
docker inspect image 230882/my-first-nginx-custom-image:v3
docker inspect 230882/my-first-nginx-custom-image:v3 --format='{{.Config.Labels}}'
docker inspect 230882/my-first-nginx-custom-image:v3 --format='{{json .Config.Labels}}'
docker inspect 230882/my-first-nginx-custom-image:v3 --format='{{json .Config.Labels}}' | jq

#Container:
docker inspect nginx-container-2
docker inspect nginx-container-2 --format='{{.Config.ExposedPorts}}'
docker inspect nginx-container-2 --format='{{.Config.Image}}'
docker inspect nginx-container-2 --format='{{.NetworkSettings.Networks.bridge.IPAddress}}'
docker inspect nginx-container-2 --format='{{ (index (index .NetworkSettings.Ports "80/tcp") 0).HostPort }}'

===========Check log
docker logs da0d00824406

############# Volume #################

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