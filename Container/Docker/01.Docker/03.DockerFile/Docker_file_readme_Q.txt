?? Define Dockerfile, what it contains?

?? Advantages of having Dockefile

??(01) In nginx install vim automatically in dockerfile.
    - Use version 1.27.0 & install vim
    - Build, Run and verify by login into container.

??(02) In Nginx base-os use index.html from current folder in dockerfile.
    - Build,tag and run from local
    - Build push to hub and run from hub.

?? Run an express app have hello world in /, Post /register & get users route.
    - initialize and use dependencies express@4.19.2 & body-parser@1.20.2 
    - write code in index.js inside src
        - Have GET / for hello world.
        - POST /register for registering a user
            - Check user already exist and body contains the userID key.
        - GET /users to list all registered user
        - Listen on port 3000
        - Test all functionality(in-memory)
    - Write dockerfile and containerize the application
        - Use node:22
        - Demonstrate data loss during"docker stop" and how its not happening in "docker pause"
?? Reduce the image size
    - By using alpine image
        - why intermediate layer doesn't have hash-id
    - Prove all files in context is copies to the docker host, increase image size and build time.
        - Which command does context transfer.
    - How to reduce image size and build time using context copy.
    - use COPY . . and still reduce size &build time
    - ignore test.js file in recursive folder.
    
?? When inspecting an image with docker history, you see that one RUN layer adds 500 MB to the image size, while the very next RUN layer removes those files and shows a size of only 1 KB. What is the effect on the final image size?
 
?? Run an express app to serve hello world in / route
    - Change port & app name as environment variable.
    - Chnage the port with out building image
    - Chnage the port using file.