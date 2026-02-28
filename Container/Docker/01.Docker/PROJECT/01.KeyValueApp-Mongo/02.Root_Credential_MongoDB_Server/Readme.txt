% vi start-db.sh
<update the script>
% chmod +x start-db.sh
% ./start-db.sh
% docker ps
% docker logs mongodb

% docker exec -it mongodb mongosh
test> show dbs;
MongoServerError[Unauthorized]: Command listDatabases requires authentication
test> use admin;
switched to db admin
admin> show collections;
MongoServerError[Unauthorized]: Command listCollections requires authentication
admin> exit

% docker exec -it mongodb mongosh -u root-user -p root-password
test> show dbs;
admin   100.00 KiB
config   12.00 KiB
local    72.00 KiB
test> use admin;
switched to db admin
admin> show collections;
system.users
system.version
admin> exit

Note: 
% docker exec -it mongodb mongosh -u root-user -p root-password --authenticationDatabase admin