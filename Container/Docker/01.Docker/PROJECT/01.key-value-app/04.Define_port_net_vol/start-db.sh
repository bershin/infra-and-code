CONTAINER_NAME="mongodb"
MONGODB_IMAGE="mongodb/mongodb-community-server"
MONGODB_TAG="7.0.22-ubuntu2204"
# Root Credential: root-user/root-password
ROOT_USERNAME="root-user"
ROOT_PASSWORD="root-password"

KEY_VALUE_DB="key-value-app"
KEY_VALUE_DB_USER="key-value-app"
KEY_VALUE_DB_PASSWORD="key-value-app"

CONTAINER_NETWORK="key-value-network"
CONTAINER_PORT=27017
HOST_PORT=27017

VOLUME_NAME="key-value-data"
VOLUME_PATH="/data/db"

docker run -d --rm --name $CONTAINER_NAME \
    -e MONGO_INITDB_ROOT_USERNAME=$ROOT_USERNAME \
    -e MONGO_INITDB_ROOT_PASSWORD=$ROOT_PASSWORD \
    -e KV_DATABASE=$KEY_VALUE_DB \
    -e KV_USER=$KEY_VALUE_DB_USER \
    -e KV_PASSWORD=$KEY_VALUE_DB_PASSWORD \
    --network $CONTAINER_NETWORK \
    -p $HOST_PORT:$CONTAINER_PORT \
    -v ./db-config/mongo-init.js:/docker-entrypoint-initdb.d/mongo.js:ro \
    -v $VOLUME_NAME:$VOLUME_PATH \
    $MONGODB_IMAGE:$MONGODB_TAG
