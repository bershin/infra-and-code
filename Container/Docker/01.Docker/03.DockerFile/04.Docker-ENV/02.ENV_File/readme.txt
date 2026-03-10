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
create .env.prod and update environment.
include env in .dockerignore
% docker run --rm --env-file ".env.prod" -p 5002:5000 -d env-docker:v1
% curl http://localhost:5002
% docker run --rm --env-file ".env.dev" -p 3002:3000 -d env-docker:v1