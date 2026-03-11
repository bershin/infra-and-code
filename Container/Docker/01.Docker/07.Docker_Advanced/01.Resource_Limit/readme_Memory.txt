=========See all options for memory
% docker run --help | grep memory

% docker run -d --rm --name mongodb mongodb/mongodb-community-server:7.0-ubuntu2204
% docker stats -> 79.08MiB / 7.654GiB used

% docker run -d --name mongodb --memory="20m" mongodb/mongodb-community-server:7.0-ubuntu2204
% docker ps -a -> No container running, In exited status
% docker inspect mongodb -> "OOMKilled": true,

% docker run -d --name mongodb --memory-reservation="80m" --memory="100m" mongodb/mongodb-community-server:7.0-ubuntu2204
% docker stats -> 80.37MiB / 100MiB, Terminate if container consumes more than 100Mib. Make sure container gets 80MiB all time.

% docker run -d --name mongodb --memory="20m" --memory-swap="200m" mongodb/mongodb-community-server:7.0-ubuntu2204
# 200-20=180MiB of disk space is allocated for swap.
% docker stats ->
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O         BLOCK I/O         PIDS 
d259e2776773   mongodb   0.88%     19.78MiB / 20MiB    98.89%    1.17kB / 126B   3.67MB / 67.5MB   34 