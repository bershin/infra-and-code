?? What is Pod
Smallest & simplest deployment unit/object that you create in a kubernetes cluster to run containers.
- Pod represent a single instance of a running process(an application) in your cluster.
- Application deployed as Container which are encapsulated into pods
- A pod can encapsulate one or more containers(Multiple container).
    - A pod allows container to share storage and network resource.
    - Container of same kind(nginx) is not recommended in a pod. Different kind like Helper container(side-car) -> Data pusher/puller, Proxies - allowed.
    - Pods can communicate with each other across namespace without policies by default.
    - We can set health probe in each containers so thay can restart or stop recieving traffic if considered unhealthy.
- Pods pull image from -> Dockerhub, github packages, Google Artifact Registry, Azure Container registry, AWS Elastic container registry

?? Pod lifecycle: Different phases of a Pods lifecycle.
1. Create Pod
    - "Pending": One or more containers are not ready to run.
        - Pod to be scheduled in Node.
        - Container images will be downloaded(Container creating)
    - "Running": All containers have been created and at least one is still running or in the process of starting or restarting.
    - <Optional>(jobs):
        - Succeeded: All container in the Pods have terminated successfully and will not be restarted.
        - Failed: All containers in the Pod have terminated and at least one container has terminated in failure(non-zero exit code.)
    - "Unknown": The pods status could not be obtined, either due to communication error with the Node running the pod or due to some other issue.

?? Understand how Pods handle container errors:
Container creating/running -> Crashes -> Restart policy applies
    - Always, InFailure, Never:
        - No: Container remains exited with error code.
        - Yes: CrashLoopBackOff (restart container, Wait for exponential backoff)
            - K8s will delay(up to 5min gradually) the restart based on the failure.
            - exponential backoff limit is reset once the pod is started successfully.
    

?? Spin you first pod with nginx image
% kubectl version
% kubectl config current-context
% kubectl config set-context minikube
% kubectl run --help
% kubectl run nginx --image=nginx:1.27.0
% kubectl get pod # Check if its running state
% kubectl describe pod nginx # fetch ip
% curl <ip> # fails

% kubectl run -it alpine --image=alpine:3.20 sh
> apk add curl
> curl <ip> fail
> curl nginx -> fail
> exit
% kubectl get pods
(see the restart)
-> See log of all containers in the pod
% kubectl logs nginx 
-> See logs of previous pod if the pod keeps on crashing
% kubectl logs -p nginx
-> See log of one containers in that pod
% kubectl logs nginx -c nginx
% kubectl delete pod alpine

% kubectl expose pod nginx --type=NodePort --port=80
% kubectl get service
% kubectl exec -it alpine -- sh
> curl 10.109.122.65 (Nodeport ip, from kubectl get svc)
> curl nginx

?? Prove recreating pod will not impact connecting via service ip.
% kubectl delete pod nginx
> curl 10.109.122.65 - fail
% kubectl run nginx --image=nginx:1.27.0
> curl 10.109.122.65 - success

?? Delete pods & service
kubectl delete service nginx
kubectl delete pod nginx
kubectl delete pod alpine

?? Create an express color web page application and access it deploy it via docker and kubernetes and access
% npm init -y
% npm i --save-exact express@4.19.2
update start in package.json
% docker build -t color-api .
% docker images | grep color-api
% docker run -p 8088:80 color-api:latest
http://localhost:8088

% docker tag color-api:latest 230882/color-api:v1
% docker push 230882/color-api:v1
% kubectl run color-api --image=230882/color-api:v1
% kubectl get pod
% kubectl describe pod color-api -> get ip
% kubectl run -it alpine --image=alpine:3.20 sh
> apk add curl
> curl http://10.244.0.13
> exit

?? Difference between imperative, imperative with config, declarative
1. Imperative mgmt with kubectl
    - Main commands
        - kubectl create <resource> [config]
        - kubectl delete <resource> 
        - kubectl expose <resource> <name
        - kubectl [get|describe|logs]
    - Pros
        - Lowest learning curve
        - Commands transparently communicate changes via single word actions.
        - Single step to male changes to the cluster.
    - Cons
        - Not possible to save template for creating new objects.
        - No change review nor audit trail possible.
        - No records of what has been created/deleted(only what is in the cluster)
2. Imperative mgmt with config files
    - Main commands
        - kubectl create -f <filename>
        - kubectl delete -f <filename>
        - kubectl replace -f <filename>
        - kubectl [get|describe|logs]
    - Pros
        - Config files can be committed, reviewed and audited.
        - File provide a template for creating new objects.
        - Simpler than declarative management.(Saying k8s what to do, not relying on the underlying mechanism to take care)
    - Cons
        - More suitable for single files rather than directories.
        - Require familarities with the object schemas for each object being managed.
        - Does not persist updtes made outside the configuration files.
3. Declarative mgmt with kubectl
    - Main commands
        - kubectl apply -f <filename>
        - kubectl delete -f <filename>
        - kubectl diff -f <filename>
        - kubectl [get|describe|logs]
    - Pros
        - Persist updates made to live objects even if not reflected in the configuration files.
        - Better support for automatically identifying necessary operations for each object.
    - Cons
        - Highest learning curve.
        - Partial updtaes are more complex to understand and debug.
        - Live objects state might not be entirely reflected in the configuration files.

