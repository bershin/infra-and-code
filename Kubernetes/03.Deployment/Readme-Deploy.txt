
kubectl create deployment my-deploy --image=230882/deploy-nginx:v1 --replicas=3
kubectl get deploy
kubectl get deploy my-deploy -o yaml
kubectl get rs
kubectl describe deploy my-deploy

kubectl rollout history deployment my-deploy 
kubectl annotate deployment my-deploy kubernetes.io/change-cause="Inital deploy"
kubectl scale --replicas=5 deploy my-deploy
kubectl expose deploy my-deploy --type=LoadBalancer --port=80 --target-port=8080 --name=deploy-svc

kubectl set image deploy my-deploy deploy-nginx=230882/deploy-nginx:v2
kubectl rollout status deploy my-deploy
kubectl get rs

kubectl rollout history deploy
kubectl annotate deployment.apps/my-deploy kubernetes.io/change-cause="v2 update"
kubectl rollout history deploy

kubectl rollout history deploy my-deploy --revision=2

kubectl rollout undo deploy my-deploy
kubectl rollout undo deploy my-deploy --to-revision=1

kubectl rollout restart deploy my-deploy

kubectl delete deploy my-deploy