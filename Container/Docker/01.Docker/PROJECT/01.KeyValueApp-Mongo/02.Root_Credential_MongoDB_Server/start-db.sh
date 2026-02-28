CONTAINER_NAME="mongodb"
MONGODB_IMAGE="mongodb/mongodb-community-server"
MONGODB_TAG="7.0.22-ubuntu2204"
# Root Credential: root-user/root-password
ROOT_USERNAME="root-user"
ROOT_PASSWORD="root-password"
docker run -d --rm --name $CONTAINER_NAME \
    -e MONGO_INITDB_ROOT_USERNAME=$ROOT_USERNAME \
    -e MONGO_INITDB_ROOT_PASSWORD=$ROOT_PASSWORD \
    $MONGODB_IMAGE:$MONGODB_TAG
