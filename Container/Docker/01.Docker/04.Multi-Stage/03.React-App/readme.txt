% npx create-react-app --template typescript containerize-react-app
% cd containerize-react-app
% npm start -> See package.json(Find the js script which this invokes, who is responsible for live update)
Webbrowser:
% http://localhost:3000
On the other terminal:
% vi src/App.tsx
Webbrowser: Check the change immediately happens.
% http://localhost:3000

Build for production:
---------------------
% npm run build -> look for "build" folder, also look 'static' file that get created 
% npx http-server@14.1.1 build
% http://localhost:8080
Note: Every time you update build t 

Dockerize:
$ vi .dockerignoe -> node_modules & build folder
% vi Dockerfile -> Write single stage & multistage & test.

% docker build -t react-app-ss:v1 -f Dockerfile-ss .
% docker run --rm -it react-app-ss:v1 sh
> ls

% docker build -t react-app-ms:v1 -f Dockerfile-ms .
% docker run --rm -d -p 9000:80 react-app-ms:v1