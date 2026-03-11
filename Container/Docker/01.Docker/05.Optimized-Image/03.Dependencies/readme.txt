% docker build -t docker-deps:v1 -f Dockerfile.deps .
% docker run --rm -d -p 3005:3000 docker-deps:v1
% curl http://localhost:3005