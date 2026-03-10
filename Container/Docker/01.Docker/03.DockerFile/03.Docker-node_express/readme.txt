# Express app to create user and check them
% npm init -y # Create package.json file
% npm install express@4.19.2 body-parser@1.20.2 --save-exact # update package.json file
Write code in index.js to have route & listen to port.
Update package.json to have start
% npm start
curl http://localhost:3000
Use postman to test the post request
% docker build -t express_app:v0.0.1 .
% docker run -p 3000:3000 --name expressapp  express_app:v0.0.1


?? Reduce the image size
- use image "node:22-alpine"
    - using "docker history <image-id>" compare the size
    - intermediate layer is not used to tag with image name, so cleaned by docker.
- Prove all files in context is copies to the docker host, increase image size and build time.
    - $ mkfile -n 5g large-file
    - $ docker build -t test-docker . (takes long time to build, see transferring context)
    - $ docker images (see more than 5 GB)
- How to reduce image size and build time using context copy.
    - copy index.js index.js (instead of COPY . .) 
        - ADD/COPy transfer files in context from client to docker host.
    - $ docker build -t test-docker .
    - $ docker images 
- use COPY . . and still reduce size &build time
    - use .dockerfile to prevent largefile/folders(node_modules, artifact, .git) and sensitive data to sent to docker daemon as part of build. 
    - Ignore files in recursive folders using **/*.test.js.
    - Check if ignored using "docker exec" command.

?? When inspecting an image with docker history, you see that one RUN layer adds 500 MB to the image size, while the very next RUN layer removes those files and shows a size of only 1 KB. What is the effect on the final image size?
    - The final image will still be appox 500mb larger because the files added in the first layer still exist in that intermediate layer, even though they are not visible in the final container filesystem.