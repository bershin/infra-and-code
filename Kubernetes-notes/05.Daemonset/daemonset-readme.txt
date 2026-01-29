Ensures all node gets a copy of the pod.
- When node are added daemonset create pod on the node.
- When a node are removed pod on that node is garbage collected.
- When daemonset is deleted it deletes all pod on the nodes.

UseCases:
- Running "cluster storage daemon" on all node
- Running "logs collector daemon" on all node
- Running "node monitoring daemon" on all node

kubectl apply -f .
kubectl get ds