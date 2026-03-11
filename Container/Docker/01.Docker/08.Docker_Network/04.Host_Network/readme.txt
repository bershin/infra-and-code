?? Prove host network maximum network performance can be achieved by eliminating the NAT(network address translation) layer. Drawback: it removes all network isolation between the container and the host which is a significant security concern.
% docker run -d --name webserver --network host nginx:1.27.0
% docker ps
% docker inspect <container_name> -> no ip address, because no isolation between host & container network.
% curl http://localhost -> Works in linux, not in mac(docker desktop is vm)
% docker run -d --network host nginx:1.27.0
% docker ps -a -> See the container in exit status
% docker logs happy_cohen --> The port is already taken by webserver

########### What should be used instead.
% docker run --rm -d --network app-net -p 80:80 nginx:1.27.0