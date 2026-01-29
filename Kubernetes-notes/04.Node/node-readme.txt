Group of node across region form a node pool
each node has label as cloud.google.com/gke-nodepool:default-pool

create another nodepool.

kubectl get pods -o wide