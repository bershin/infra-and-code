?? Prove container do not restart for non-zero exit code.(use busybox)
% docker run -d --name no_restart busybox sh -c "sleep 3; exit 1"
% docker ps
% docker ps -a
% docker inspect no_restart 

?? Prove container keeps on restarting continiously for non-zero exit code.(use busybox)
% docker run -d --name keep_restart_fail --restart on-failure busybox sh -c "sleep 3; exit 1"
# keep on restart when the container exit with non-zero code
% docker inspect no_restart -> look for restart count.

?? Prove container restarts only 3 times for non-zero exit code and Do not restart for zero exit code(use busybox)
% docker run -d --name restart_three_fail --restart on-failure:3 busybox sh -c "sleep 3; exit 1"
# Restart the container for three times,when it exit with non-zero code
% docker inspect no_restart -> look for restart count.

% docker run -d --name restart_success --restart on-failure:3 busybox sh -c "sleep 3; exit 0"

?? Restart the container, inspite of exit code. express application tries to connect to database which is in starting state.
% docker run -d --name restart_always --restart always busybox sh -c "sleep 3; exit 0"
% docker inspect restart_always | grep Restart
% docker stop restart_always -> Only way to stop the container.
Note: Only way this container get started is 
    - Manually start using `docker start`
    - Docker daemon gets restarted.(docker desktop restart)

?? Do not start the container on docker daemon restart.
% docker run -d --name restart_unless --restart unless-stopped busybox sh -c "sleep 3; exit 0"
% docker ps
Note: The container will not get started when the docker daemon is restarted.