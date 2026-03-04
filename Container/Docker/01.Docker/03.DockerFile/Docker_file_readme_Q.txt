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