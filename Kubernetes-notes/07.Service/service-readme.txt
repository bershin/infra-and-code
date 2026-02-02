=========Load Balancer (Layer-4 External LB)

=========Nodeport (Layer-4 External LB)
- range -> 30000 to 32768. Firewall needs to be allowed
- Not used in prod -> http://<Node-PublicIp>:<NodePort>
- Used for testing to save loadbalancer cost.

http://34.27.67.60:30080/

===========Cluster-IP (Layer-4 internal load balancer)
Internal client request. 

kubectl apply -f ClusterIP-manifest.yaml 
kubectl exec -it cip-demo -- /bin/bash
- curl http://34.118.228.110 
- curl http://curl-service.default.svc.cluster.local

===========Headless service (Layer-4 internal load balancer)
- No specific IP, instead resolves ip of the pods.
Usecase
- Statefulset
- Database cluster(cassandra, mysql)
- Messaging systems(rabbitmq, kafka)

===========Ingress service (Layer-7 external load balancer)
- Layer 7 is aware of Application(url path, host header etc)