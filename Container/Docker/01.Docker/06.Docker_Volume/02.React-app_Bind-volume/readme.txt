% npx create-react-app --template typescript containize-app-vol
% cd containize-app-vol
% npm start
% docker build -t docker-react-bind-vol:v1 -f Dockerfile.dev . 
% docker run --rm -d -v ./public:/app/public -v ./src:/app/src -p 3004:3000 docker-react-bind-vol:v1 