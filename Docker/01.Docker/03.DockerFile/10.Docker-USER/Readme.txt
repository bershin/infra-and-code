Run the container as user.
Set default user to rest of the stage.
Applies to RUN, CMD, ENTRPOINT 


docker build -t python:user1 .
docker run --name cont-10 -p 5000:5000 -d python:user1

docker exec -it cont-10 ls -l /usr/src/app
docker exec -it cont-10 env