?? Why we need docker network and its benefits?

?? Main network Drivers in docker and where it can be used

?? Docker network commands

?? Prove by default containers use bridge network driver. Using bridge network, containers can communicate with IP but not with container name from another container.

?? Prove using user defined network providing automatic service discovery via DNS, allowing containers on the same network to communicate with each other using their container names as hostnames.
    - Container has two ip and will be able to connect to the containers which are in the network that was added later.

?? Prove host network maximum network performance can be achieved by eliminating the NAT(network address translation) layer. Drawback: it removes all network isolation between the container and the host which is a significant security concern.