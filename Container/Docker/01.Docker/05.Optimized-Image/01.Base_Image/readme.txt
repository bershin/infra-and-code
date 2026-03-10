?? Prove changing the base image can change the image size in a express app
% npm init -y
% npm install express@4.19.2 --save-exact
% npm install jest@29.7.0 typescript@5.5.3 @types/express@4.17.21 --save-exact --save-dev
    - Confirm -> % cat package.json

Create & Update "Dockerfile.vanilla" use node:22 & "index.js" to just print an output.
% docker build -t image-size:vallina -f Dockerfile.vanilla .
% docker images | grep  image-size  -> check size
% docker history image-size:vallina -> Notice the layer build by us uses minimum size & no room for optimization.

Create & Update Dockerfile.slim with slim version of nodejs 22
% docker build -t image-size:slim -f Dockerfile.slim .
% docker images | grep  image-size  -> compare size reduced by 1/4
% docker history image-size:slim -> Notice the base image is small which reduced the size

Create & Update Dockerfile.alpine with slim version of nodejs 22
% docker build -t image-size:alpine -f Dockerfile.alpine .
% docker images | grep  image-size  -> compare size reduced by 1/6 of vanilla
% docker history image-size:alpine -> Notice the base image is small which reduced the size