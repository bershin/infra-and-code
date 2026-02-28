const keyValueDB = process.env.KV_DATABASE;
const keyValueUser = process.env.KV_USER;
const keyValuePassword = process.env.KV_PASSWORD;

console.log("Initializing: Key-Value DB User");
db = db.getSiblingDB(keyValueDB);

db.createUser({
  user: keyValueUser,
  pwd: keyValuePassword,
  roles: [{ role: "readWrite", db: keyValueDB }],
});
