?? Prove using user defined network providing automatic service discovery via DNS, allowing containers on the same network to communicate with each other using their container names as hostnames.
% docker network create app-net
% docker network ls
% docker network inspect app-net -> No container entry and uses bridge driver.
% docker run --rm -d --name webserver nginx:1.27.0
% docker network connect app-net webserver
% docker network inspect app-net -> See container enrty in bridge & app-net. Auto discovery enabled in app-net.

% docker run --rm -it --network app-net alpine:3.20 sh
> apk update && apk upgrade
> apk add curl
> curl <webserver_ip_app_network> -> success
> curl <webserver_name> -> success
> curl <default_bridge_ip> -> fail
> apk update 
> apk add ipconfig2
> ip route
> exit

% docker network rm app-net


#############Directly create using network
% docker run --rm -d --network app-net nginx:1.27.0