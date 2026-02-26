Set the backup command for the container
- CMD["executable", "param1", "param2"]
    CMD["param1", "param2"]
- Can be changed by "docker run"
    argument overrites CMD


docker build -t nginx-cmd:v1 .
docker run --name nginx-cmd -p 8080:80 -d nginx-cmd:v1
curl http://localhost:8080
docker inspect nginx-cmd --format='{{.Config.Cmd}}'
docker exec -it nginx-cmd ps aux

$ docker run -it --name nginx-cmd-3  nginx
-cmd:v1 /bin/sh
/ # ps aux
# Another terminal
docker inspect nginx-cmd-3 --format='{{.Config.Cmd}}'

