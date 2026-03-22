?? Imperative way to create a pod using config file
% kubectl create -f nginx-pod.yaml
% kubectl get pod myapp-pod
% kubectl describe pod myapp-pod
% kubectl create -f nginx-svc.yaml
% kubectl get svc myapp-svc
% kubectl describe pod myapp-svc

% kubectl run alpine-pod --image=alpine:3.20 sh
> apk --upgrade add curl
> curl <nodePort-ip>

% kubectl delete -f nginx-pod.yaml

> curl <nodePort-ip> # fail

% kubectl create -f nginx-pod.yaml

> curl <nodePort-ip> # success

?? Create config yaml using imperative command
% kubectl run clour-api --image=230882/color-api:v1 --dry-run=client -o yaml > colour-api-pod.yaml
% kubectl expose pod clour-api --type=NodePort --port=80 --dry-run=client -o yaml > colour-api-svc.yaml
?? How does the service know which pod to send the traffic.
    - The spec.selector field is Service is configured to match the metadata.labels of the target pods.

?? Limitation of imperative with config files.
- The replace command tries to make the live object exactly match the local YAML file. The live pod has the system assigned fields like nodename that is not in the local file. The comand fails because it tries to change the immutable field.

?? Compare what kubernetes look the nginx pod & what we have.
% cat nginx-pod.yaml
% kubectl get pod nginx-pod -o yaml
# change image nginx:1.27.0 to nginx:1.27.0-alpine in nginx-pod.yaml
% kubectl replace -f nginx-pod.yaml
# Even though image field can be changed. It says Volume, VolumeMount, Service Account was mentioned in the config file and it set by K8s already. So we may need to delete and recreate it using imperative.
% kubectl delete -f nginx-pod.yaml -f nginx-svc.yaml
% kubectl create -f nginx-pod.yaml
% kubectl describe pod nginx-pod

?? How declarative with config files can overcome the limitation.
# change image nginx:1.27.0-alpine to nginx:1.27.0 in nginx-pod.yaml
% kubectl apply -f nginx-pod.yaml
% kubectl get pods
% kubectl delete -f .
?? How declarative commad works with files and directories
% kubectl apply -f .
(or)
% cd ..
% kubectl apply -f imperative_declarative-manifest
# kubectl 'apply' calculates the difference between 
    - last applied configurations
    - the current live state.
    - The new configuration file
 to perform a three way merge and only 'patch' the necessary changes. This preserve changes made by other controllers(like annotations added by service mesh) that are not in local file.


% kubectl diff -f imperative_declarative-manifest
# change image nginx:1.27.0 to nginx:1.27.0-alpine in nginx-pod.yaml
% kubectl apply -f imperative_declarative-manifest
% kubectl describe pod nginx-pod
# Check the pod was not deleted and create but the container does. Compare with event and container section.
% kubectl get pod nginx-pod -o yaml
# See the last-applied configuration, where the config in our yaml is converted into a json file for reference. 

?? Bring Imperative config pod to declarative pod config
% kubectl create -f nginx-pod.yaml
# Check for last applied config (% kubectl create --save-config -f nginx-pod.yaml)
% kubectl apply -f .
# See a warning message