% docker run -d --name mongodb mongodb/mongodb-community-server:7.0.22-ubuntu2204
% docker ps -> look its up for some seconds.
% docker logs mongodb
% docker exec -it mongodb mongosh
test> show dbs;
test> use admin
admin> show collections;
admin> exit