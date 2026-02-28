source .env.network
source .env.volume

if [ "$(docker network ls --filter name=^${CONTAINER_NETWORK}$ --format '{{.Name}}')" = "${CONTAINER_NETWORK}" ]; then
    echo "Network ${CONTAINER_NETWORK} already exists."
else
    echo "Creating network ${CONTAINER_NETWORK}..."
    docker network create ${CONTAINER_NETWORK}
fi

if [ "$(docker volume ls -q --filter name=${VOLUME_NAME})" ]; then
    echo "Volume ${VOLUME_NAME} already exists. Skipping creation...."
else
    echo "Creating volume ${VOLUME_NAME}..."
    docker volume create ${VOLUME_NAME}
fi