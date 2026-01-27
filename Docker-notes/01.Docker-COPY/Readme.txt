# Run a docker container from base image and Check
docker run --name my-nginx -p 8080:80 -d nginx
docker ps
curl http://localhost:8080

# Create a custom image and run docker from the local custom image
docker build -t my-first-nginx-custom-image:v1 .
docker run --name my-first-custom-container -p 8081:80 -d my-first-nginx-custom-image:v1
curl http://localhost:8081
docker exec -it my-first-custom-container ls -l /usr/share/nginx/html/


# Create a custom image and push to dockerhub and run docker from dockerhub
docker build -t my-first-nginx-custom-image:v3 .
docker tag my-first-nginx-custom-image:v2 230882/my-first-nginx-custom-image:v2
docker push 230882/my-first-nginx-custom-image:v2
docker run --name nginx-container-2 -p 8082:80 -d 230882/my-first-nginx-custom-image:v2
curl http://localhost:8082
docker exec -it my-first-custom-container /bin/bash


# Cleanup
docker stop my-nginx
docker rm my-nginx
docker rmi my-first-nginx-custom-image:v1

# Clean all
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -q)


