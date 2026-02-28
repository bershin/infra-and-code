- Create a docker compose file and run a mongodb service on port "27017" using community image "7.0.22-ubuntu2204"
    % vi compose.yaml
    % docker compose up
- Check the default network & container name creted.
    - % docker ps
    - % docker network ls
- Connect to the container by spining another docker container and check the db details.
% docker run -it --rm --network 01run-mongodb_default mongodb/mongodb-community-server:7.0.22-ubuntu2204 mongosh mongodb://01run-mongodb-db-1
test> show dbs;
admin   40.00 KiB
config  12.00 KiB
local   40.00 KiB
test> use admin;
switched to db admin
admin> show collections;
system.version
admin> db.getUsers()
{
  users: [
    {
      _id: 'admin.root',
      userId: UUID('82a5ae20-1062-4f82-a06d-5ee7bbe05699'),
      user: 'root',
      db: 'admin',
      roles: [ { role: 'root', db: 'admin' } ],
      mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
    }
  ],
  ok: 1
}
admin> use kvdb
switched to db kvdb
kvdb> show collections;

kvdb> db.getUsers()
{ users: [], ok: 1 }
kvdb> use admin
switched to db admin
- Remove the docker container and the network created
% docker compose down