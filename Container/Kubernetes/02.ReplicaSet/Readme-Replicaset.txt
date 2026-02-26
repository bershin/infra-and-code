Maintain a set of replica pods
HA 
Scale the pods

kubectl create -f Replicaset.yaml 
kubectl get rs
kubectl describe rs
while true; do curl -s http://34.30.80.106/ | grep Hostname; sleep 1; done
kubectl get pod
kubectl delete pod nginx-rs-8h4cm
# Update replica - 3 ways
kubectl apply -f Replicaset.yaml
kubectl scale --replicas=3 rs nginx-rs
kubectl edit rs nginx-rs
kubectl delete rs nginx-rs
kubectl delete -f Replicaset.yaml