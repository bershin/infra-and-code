===========GKE============
kubectl run pod-demo-test --image=230882/pod-demo:v3
kubectl get pod
kubectl describe pod <pod>
# See the node they run under
kubectl get pod -o wide
kubectl get pod <pod> -o yaml
kubectl logs <pod>
# Live logs, see application error.
kubectl logs -f <pod>
kubectl delete pod <pod>
kubectl exec -it pod-demo-test -- ls -l /usr/share/nginx/html/
kubectl exec -it pod-demo-test -- /bin/sh


kubectl expose pod pod-demo-test --type=LoadBalancer --port=80 --name=nginx-svc
kubectl get svc
kubectl describe svc nginx-svc
# See the selector
kubectl get svc nginx-svc -o wide
kubectl get svc nginx-svc -o yaml
kubectl delete svc nginx-svc
Browser -> http://34.132.147.250/