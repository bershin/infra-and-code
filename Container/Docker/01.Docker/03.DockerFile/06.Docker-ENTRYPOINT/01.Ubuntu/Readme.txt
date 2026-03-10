Set the main command for the container
- ENTRYPOINT["executable", "param1", "param2"]
- arguments append entrypoint "docker run ARG"
- Can be changed by "docker run --entrypoint executable -c "param1 param2""

docker build -t entrypoint:v1 .
docker run --name ep-2 entrypoint:v1

docker run --name ep-3 entrypoint:v1 bershin

docker run --name ep-4 --entrypoint "/bin/sh" entrypoint:v1 -c "echo IAM YOUR DREAM"
