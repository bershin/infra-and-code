To prevent a single misbehaving or resource-intensive container from consuming all available resources and degrading the performance or stability of other containers and the host itself.
=========See all options for cpu
% docker run --help | grep cpu

=========CPU limits (Hard limit)
% docker run --rm -d --name cpu-decimals --cpus=0.5 busybox sh -c "while true; do :; done"
% docker stats -> Cpu percentage oscillate around 50%

% docker run --rm -d --name cpu-decimals --cpus=1.5 busybox sh -c "while true; do :; done"
% docker stats -> Cpu percentage oscillate around 100% instead 150%
Note: Because container only runs one busy loop process: This loop is single-threaded, meaning it can only run on one CPU core at a time.

% docker run --rm -d --name cpu-decimals --cpus=1.5 busybox sh -c "while true; do :; done & while true; do :; done"
% docker stats -> Cpu percentage oscillate around 150%
Note: The container will be throttled and will not be allowed to use more than 75% of a single CPU core's processing power at any given time.

=========CPU share(Soft limit); pin/bound to a CPU, here its 0
# Say one container to be given 80% and other 20% of cpu
% docker run --rm -d --name cpu-share_low --cpu-shares=512 --cpuset-cpus=0 busybox sh -c "while true; do :; done"
% docker stats -> Cpu percentage oscillate around 100%, because 512 us total share.
% docker run --rm -d --name cpu-share_high --cpu-shares=2048 --cpuset-cpus=0 busybox sh -c "while true; do :; done"
% docker stats -> High gets 70% and low get 30%. total share is 2560 and divide proposinally based on share of each container.
Note: When there is a constrain in cpu, use soft limit.

=========CPU quota; equivalent to hard limit, microseconds
% docker run --rm -d --name cpu-quota --cpu-period=100000 --cpu-quota=75000 busybox sh -c "while true; do :; done"
% docker stats -> Cpu percentage oscillate around 75%



