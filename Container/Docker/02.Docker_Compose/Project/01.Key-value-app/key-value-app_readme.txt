01. Create a docker compose file and run a simple mongodb service on port 27017 using community image 7.0.22-ubuntu2204
- Check the network created and name of container.
- Connect to the container by spining another docker container and check the db details.
- Remove the docker container and the network created
- Connect to the database.

02. Docker compose for database with network, volume & environment file.
- Add root credentials and new user with key-value-db database
- Best practice to avoid sensitive information checked into git.
- Create init script for user creation in mongodb database.
    - Bind volume to create database and user.
- Volume for persistence database storage.
- Create a network and attach to the db service.
- Name the application instead of using default one.
- Connect to the database.

03. Docker compose for backend with network, port, volume & environment.
- Copy the backend folder
- Update the compose file with backend.
- build image before bringing docker up
- Test endpoints using postman
- Enable Hot reloading 
    - Use either watch or bind volume which ever works for you.