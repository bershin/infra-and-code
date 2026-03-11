?? Prove by default containers use bridge network driver. Using bridge network containers can communicate with IP but not with container name
% docker network ls
% docker run --rm -d --name webserver nginx:1.27.0
% docker network inspect bridge -> See the container get registered 7 its IP & name.
% docker inspect webserver -> See the container ip,DNS is null.(Auto discovery disabled)

% docker run --rm -it ubuntu:24.04 sh
> apt update && apt upgrade
> apt install curl
> curl <webserver_ip> -> success
> curl <webserver_name> -> fails "curl: (6) Could not resolve host: webserver"
> exit

