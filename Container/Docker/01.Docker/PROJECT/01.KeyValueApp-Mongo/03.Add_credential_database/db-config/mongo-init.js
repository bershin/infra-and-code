const keyValueDb = process.env.KV_DATABASE
const keyValueDbUser = process.env.KV_USER
const keyValueDbPassword = process.env.KV_PASSWORD

const db = db.getSiblingDB(keyValueDb);

db.createUser({
  user: keyValueDbUser,
    pwd: keyValueDbPassword,
    roles: [
      {
        role: "readWrite",
        db: keyValueDb
      }
    ]
});