Node-pool level setting:
- Increase the avaiability of workloads by increasing and decreasing the node based on  workload resource demand.
- Scale in & scale out ( based on min & max size set in node pool)
- Increase when scheduler reports unschedulable. If node in idle state, node will scale in by deleting node.
- Control cost
- Only available in standard cluster(node pool level).

Test:
Scale the pod(resource) and see the node getting scaled.
kubectl scale deploy <deploy> --replicas=20

======= HPA:
Increase & Decrease pods in response to:
- Workload cpu/memory utilization
- Custom metrics report from within Kubernetes cluster.
- External metrics(LB, messaging service, etc)
- Custom metrics from Managed Service for Prometheus.

HPA can be applied to:
- Replicaset & Replication controller
- Deployment
- Statefulset

Metric server, should be running: (Dedcated for auto scaling)
- Collect metrics from "Kubelets" and exposes them in kubernetes Apiserver through Metrics API
- Metric API can also be accessed by "kubectl top", making it easier to debug autoscaling pipelines.
- Collect metrics in every 15 seconds. Autoscalar also query metric server every 15 sec.
- Resource efficiency, 1 milli core of CPU / 2 MB of memory for each node in cluster.
- Used for HPA and VPA
# kubectl get deploy -n kube-system | grep metrics-server
# kubectl autoscale deployment my-app --max 6 --min 4 --cpu-percent 50
# kubectl apply -f .
# kubectl run -it load-generator -rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://<cip>; done"
# kubectl top pod
# kubectl get hpa / pod / node
- see the hpa % increase and pod get increases to normalize it back below thresold
- Stop the request and see the pod is scaled in, also see the hpa.

======= VPA:
Autoscalar has to be enabled in node pool.