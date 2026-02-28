source .env.db
source setup.sh

MONGODB_IMAGE="mongodb/mongodb-community-server"
MONGODB_TAG="7.0.22-ubuntu2204"
# Root Credential: root-user/root-password
ROOT_USERNAME="root-user"
ROOT_PASSWORD="root-password"

KEY_VALUE_DB="key-value-app"
KEY_VALUE_DB_USER="key-value-app"
KEY_VALUE_DB_PASSWORD="key-value-app"

# source .env.network
CONTAINER_PORT=27017
HOST_PORT=27017

# source .env.volume
VOLUME_PATH="/data/db"

if [ "$(docker ps -q --filter name=^${DB_CONTAINER_NAME}$)" ]; then
    echo "Container ${DB_CONTAINER_NAME} is already running."
    echo "Stopping the container ${DB_CONTAINER_NAME} removes them..."
    echo "To stop the container with: docker kill ${DB_CONTAINER_NAME}"
    exit 1
else
    echo "Starting container ${DB_CONTAINER_NAME}..."
    docker run -d --rm --name $DB_CONTAINER_NAME \
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
fi