?? Why we need docker network and its benefits?
It is used to isolate and connect containers. Docker networking provides the infrastructure to make inter-container and external communication possible while maintaining the security and isolation benefits ofcontainers.
- Containers in a Docker network receive a unique IP address. This address allows other containers on the same netwoek to communicate with it.
- We can also assign names to containers and use them as aliases. This is best practice, since IP addresses may change on container recreation and names are more stable.
- Containers in bridge networks can be made reachable from the host network by exposing ports
- Containers can be connected to multiple networks and will receive a unique IP address per network.


?? Main network Drivers in docker and where it can be used
Bridge:
    - Creates a private network on the host machine where your containers can communicate with each other.
    - Suitable for most single-host scenarios.
Host:
    - Removes network isolation between the container and the host.
    - Useful for maximum performance when strict isolation is not required.
None:
    - Disable all networking for a container.
    - Rarely used, but can be helpful for specific isolation requirement.
Overlay:
    - Designed for multi-host networking, allowing container on different hosts to communicate directly.
    - Essential for creating swarm clusters or distributed applications.
Macvlan:
    - Assign a MAC address to the containers, making them appear as a physical device.

?? Docker network commands
% docker network ls
% docker network create <network_name>
% docker network connect <network_name> <container_name>
% docker network inspect <network_name> 
% docker network prune.