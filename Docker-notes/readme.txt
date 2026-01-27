####################### Docker command ########################

==============Spin a docker container
docker run --name <name_of_container> -p <host_port:<container_port> -d <image_name>
docker run --name my-nginx -p 8080:80 -d nginx
curl http://localhost:8080
================Verify running docker containers
docker ps
===============Stop a docker container
docker stop <container_name>
docker stop my-nginx
================Verify running/stopped docker containers
docker ps -a
===============Remove a docker container
docker rm <container_name>
docker rm my-nginx
===============Stop and remove docker container in one command
docker rm -f <container_name>
docker rm -f my-nginx
==============Stop and remove all container
docker rm -f $(docker ps -aq)
=================Build a docker image using 01.DockerBasic
docker build -t my-first-nginx-custom-image:v1 .
===============Check the image build status
docker images
==============Remove all images
docker rmi -f $(docker images -q)
===============Run the local image as container
docker run --name my-first-custom-container -p 8081:80 -d my-first-nginx-custom-image:v1
curl http://localhost:8081
===============Push the image to docker hub
docker build -t my-first-nginx-custom-image:v1 .
docker tag my-first-nginx-custom-image:v1 230882/my-first-nginx-custom-image:v1
===============Update & Push the image to docker hub
docker build -t my-first-nginx-custom-image:v2 .
docker tag my-first-nginx-custom-image:v2 230882/my-first-nginx-custom-image:v2
docker push 230882/my-first-nginx-custom-image:v2
==============Run the container from github
docker run --name nginx-container-2 -p 8082:80 -d 230882/my-first-nginx-custom-image:v2
curl http://localhost:8082