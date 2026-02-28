% vi start-db.sh
<Update port network and volume>

% docker network create key-value-network
% docker network ls
% ./start-db.sh
% docker ps
% docker logs mongodb
% docker volume ls

% docker run -it --rm --name mongo-client --network key-value-network  mongodb/mongodb-community-server:7.0.22-ubuntu2204 mongosh mongodb://key-value-app:key-value-app@mongodb:27017/key-value-app
key-value-app> show dbs;
key-value-app> show collections;
key-value-app> exit

% docker kill mongodb
% docker ps
% docker volume rm key-value-data
% docker network rm key-value-network