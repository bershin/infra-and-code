####################### Docker command ########################

==============Spin a docker container
# Run from dockerhub base image
docker run --name <name_of_container> -p <host_port:<container_port> -d <image_name>
docker run --name my-nginx -p 8080:80 -d nginx
curl http://localhost:8080
# From local image
docker run --name my-first-custom-container -p 8081:80 -d my-first-nginx-custom-image:v1
# From dockerhub custom image
docker run --name nginx-container-2 -p 8082:80 -d 230882/my-first-nginx-custom-image:v2

=================Build a docker image, tag & push
docker build -t my-first-nginx-custom-image:v1 .
docker tag my-first-nginx-custom-image:v1 230882/my-first-nginx-custom-image:v1
docker push 230882/my-first-nginx-custom-image:v2 
##Require docker login## -> docker login

================Verify docker containers & images
# Only running
docker ps
# Running and stopped
docker ps -a
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