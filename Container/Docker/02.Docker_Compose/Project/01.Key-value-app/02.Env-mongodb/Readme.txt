02. Environment variables in docker compose.
- Add root credentials and new user with key-value-db database
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
- Best practice to avoid sensitive information checked into git.
    - use .env file and seperate for root and user cred
    - This will avoid git from checling out the sensitive info to repo.
- Create init script for user creation in mongodb database.
    - Bind volume to create database and user.(/docker-entrypoint-initdb.d)
    - Volume for persistence database storage.(/data/db)
- Create a network and attach to the db service.
- Change the prifix used for each object instead of default folder name.
- Start the docker & check logs
    - docker compose down -v (so no script execution id /data/db has data)
    - % docker compose up -d
    - docker compose logs -f db
    - % docker ps
- Check the connectivity
% docker run -it --rm --network key-val-app_key-value-net mongodb/mongodb-community-server:7.0.22-ubuntu2204 mongosh mongodb://kvuser:kvpassword@key-val-app-db-1/kvdb
kvdb> show dbs;
kvdb> show collections;
kvdb> exit