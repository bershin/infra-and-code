% mkdir db-config
% vi db-config/mongo-init.js
% vi start-db.sh

% docker exec -it mongodb mongosh -u root-user -p root-password --authenticationDatabase admin
test> show dbs;
admin   100.00 KiB
config   12.00 KiB
local    72.00 KiB
test> use key-value-app
switched to db key-value-app
key-value-app> db.getUsers()
{
  users: [
    {
      _id: 'key-value-app.key-value-app',
      userId: UUID('bd7f7748-33c2-4140-b891-2305ec2a0052'),
      user: 'key-value-app',
      db: 'key-value-app',
      roles: [ { role: 'readWrite', db: 'key-value-app' } ],
      mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
    }
  ],
  ok: 1
}
key-value-app> exit
% docker exec -it mongodb mongosh \
  -u "key-value-app" \
  -p "key-value-app" \
  --authenticationDatabase "key-value-app"