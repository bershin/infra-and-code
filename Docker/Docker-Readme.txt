1. How we build & deploy application(nodeJS) without containers?
- Install dependencies NodeJS itself needs. ($ apt install nodejs npm)
- Install nodeJS itself(specific version) to run our javascript files.(nvm install 20)
- Install application dependencies through package.json. (npm install)
- Optional(Build & Compilation for few language like Typescript(npm run build), Java, Go). Not for interpretted language like 
- Run our application.(node app.js)

- We may work on two application one is compatable in node18 and other on node22(nvm use 18). How do we run & manage the different version in same machine?
- What if manage multiple application running side by side(Go, Java, nodeJS) have conflict with upstream dependencies.( OpenSSL 1.1, libssl-dev, libcrypto.so)
    - Applications dynamically link to these shared libraries at runtime.(libssl.so.1.1, libssl.so.3). They do not overwrite each other.
        - /usr/lib/x86_64-linux-gnu/libssl.so.1.1
        - /usr/lib/x86_64-linux-gnu/libssl.so.3
    - OS upgrade breaks one of them.

2. How do containers come into rescue?
Container encapsulate all the dependencies and configurations necessary to run whatever applications in whatever language.
- Simplified Setup: (No need to worry about dependencies)
- Portability: Same container can run on any machine. All you need is the runtime installed in the machine that you are running.
- Consistent environment: No matter how many times you run, it builds with same setup. The container is build with same set of instruction.
- isolation: Control over network between containers and host machine are running.
- Efficient: More effecient than VM because of shared OS.
- Best resource control: Fine grain cpu & memory and set limit for containers, so it doesn't consumes resource from other container.
- Easy Scalable application: Can be scaled horizontally. 

3. Containers Vs Virtual Machines:
- isolation
    - VM: Strong isolation, Each VM has its own OS, providing complete isolation.
    - Container: Process-level isolation, Container shares the host OS kernel.
- Size/Overhead:
    - VM: Have large footprint because of guest OS and virtual hardware.
    - Container: Lightweight/minimal overhead as they share the kernel with host OS.
- Portability:
    - VM: Less portable because it is tied to specific hypervisor and guest OS configuration.
    - Container: High Portable, of platform agnostic and run consistently.

4. Docker components:
- Docker client: Docker CLI, API calls
- Docker Hosts: Docker daemon, Rest API, Containers, Image cache
- Image Registry: Docker hub
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