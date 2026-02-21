Usecase
- Mysql
- Postgres
- Cassandra
- Redis
- ElasticSearch
- Kafka
- zookeeper


When a pod restarted:
- Come with same hostname.
- Mount the same pv

Each pod will have a dedicated headless service endpoint with pod id:
- Pod-0 Endpoint: mypod-0.myhs.default.svc.cluster.local
- Pod-1 Endpoint: mypod-1.myhs.default.svc.cluster.local
(or)
Service endpoint: myhs.default.svc.cluster.local
- Headless service endpoints load balance traffic to all pods.

Commands:
kubectl get sts
kubectl get pods
kubectl get pvc
kubectl get pv
kubectl get svc
kubectl get endpoints

Conect to curl pod and connect using service endpoint(ip changes) & pod endpoint

Test:
Delete the pod and see it create with same name & mount to same volume(claim name)