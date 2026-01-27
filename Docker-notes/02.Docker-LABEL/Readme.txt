- Label
-- Add metadata to an image or container. 
-- Can have more than one labels.
-- Labels inherit from base image. if an conflict, the latest one is used

# Add labels
docker build -t my-label:v1 .
docker run --name nginx-container-2 -p 8082:80 -d my-label:v1
curl http://localhost:8082
docker exec -it nginx-container-2 /bin/bash

# Look for labels
docker inspect nginx-container-2 --format='{{.Config.Labels}}'
docker inspect nginx-container-2 --format='{{json .Config.Labels}}' | jq

