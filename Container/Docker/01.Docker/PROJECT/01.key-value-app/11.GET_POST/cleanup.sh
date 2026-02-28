source .env.db
source .env.network
source .env.volume

if [ "$(docker ps -q --filter name=^${DB_CONTAINER_NAME}$)" ]; then
    echo "Container ${DB_CONTAINER_NAME} is already running."
    echo "Stopping the container ${DB_CONTAINER_NAME} removes them..."
    docker kill ${DB_CONTAINER_NAME}
else
    echo "No running container named ${DB_CONTAINER_NAME} found."
fi

if [ "$(docker network ls --filter name=^${CONTAINER_NETWORK}$ --format '{{.Name}}')" = "${CONTAINER_NETWORK}" ]; then
    echo "Network ${CONTAINER_NETWORK} already exists."
    echo "Removing the network ${CONTAINER_NETWORK}..."
    docker network rm ${CONTAINER_NETWORK}
else
    echo "No network named ${CONTAINER_NETWORK} found."
fi

if [ "$(docker volume ls -q --filter name=^${VOLUME_NAME})" = "${VOLUME_NAME}" ]; then
    echo "Volume ${VOLUME_NAME} already exists."
    echo "Removing the volume ${VOLUME_NAME}..."
    docker volume rm ${VOLUME_NAME}
else
    echo "No volume named ${VOLUME_NAME} found."
fi