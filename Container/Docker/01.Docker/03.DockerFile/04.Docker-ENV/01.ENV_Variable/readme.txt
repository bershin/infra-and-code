% npm init -y 
% npm install express@4.19.2 --save-exact
Update index.js with node:22-alpine image
update package.json
% npm start -> test curl://localhost:5001
Update "Dockerfile" with ENV for port to 5000 
Update index.js for port to use env
Update .dockerignore
% docker build -t env-docker:v1 .
% docker run --rm -p 5001:5000 -d env-docker:v1
% docker logs -> See the updated port
test curl://localhost:5001


Change the port with out building image
% docker run --rm -e PORT=6001 -p 5001:6001 -d env-docker:v1
% docker run --rm -e PORT=5000 -e APP_NAME="hello-app" -p 5002:5000 -d env-docker:v1
% curl http://localhost:5002