ENV is available in container during run time.
WORKDIR during "cd" inside image
- Default WORKDIR is '\' if not specified (or) inherit from base image.
- Multiple WORKDIR is allowed. WORKDIR /etc;  WORKDIR nginx; RUN pwd; -> /etc/nginx
CMD - runs, when the container is starting from an image.
- only one CMD instruction is allowed. If multiple last CMD takes effect



docker build -t env-cmd:v1 .
docker run --name cmd-env -p 5000:5000 -d env-cmd:v1
curl http://localhost:5000
docker exec -it cmd-env env

docker build --build-arg MY_ENV=qa  -t env-cmd:v2 .
docker run --name cmd-env-qa -p 5001:5000 -d env-cmd:v2
curl http://localhost:5001
docker exec -it cmd-env-qa ls /app/

docker run --name cmd-env-dev -p 5002:5000 -e APP_ENVIRONMENT=dev -d env-cmd:v2
docker exec -it cmd-env-dev env