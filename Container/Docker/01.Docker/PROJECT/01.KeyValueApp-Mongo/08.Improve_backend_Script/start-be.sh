source .env.db
source .env.network

BE_CONTAINER_NAME="backend"
BACKEND_IMAGE="key-value-backend"
BACKEND_TAG="v1"

CONTAINER_PORT=3000
LOCALHOST_PORT=3000

if [ "$(docker ps -q --filter name=^${BE_CONTAINER_NAME}$)" ]; then
    echo "Container ${BE_CONTAINER_NAME} is already running."
    echo "Stopping the container ${BE_CONTAINER_NAME} removes them..."
    echo "To stop the container with: docker kill ${BE_CONTAINER_NAME}"
    exit 1
fi

echo "Builder Backend Image ${BE_CONTAINER_NAME}..."
docker build -t $BACKEND_IMAGE:$BACKEND_TAG \
    -f backend/Dockerfile.dev \
    backend/

echo "Starting container ${BE_CONTAINER_NAME}..."
docker run -d --rm --name $BE_CONTAINER_NAME \
    -e KV_DATABASE=$KEY_VALUE_DB \
    -e KV_USER=$KEY_VALUE_DB_USER \
    -e KV_PASSWORD=$KEY_VALUE_DB_PASSWORD \
    -e PORT=$CONTAINER_PORT \
    -e MONGO_HOST=$DB_CONTAINER_NAME \
    --network $CONTAINER_NETWORK \
    -p $LOCALHOST_PORT:$CONTAINER_PORT \
    $BACKEND_IMAGE:$BACKEND_TAG