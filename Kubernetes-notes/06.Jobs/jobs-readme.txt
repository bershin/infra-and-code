Job create a pod to execute a task.(Log analysis)
Usecase:
- Batch processing: ETL Jobs, Log analysis & report generation.
- Parallel processing: parallizing data analysis & image processing

# restartPolicy: Never:
- Do not restart containers after they exit.

kubectl apply -f .
kubectl get job
kubectl get pod
kubectl logs job1-ddr5q


kubectl create job job1 --image=alpine -- sh -c 'for i in 1 2 3 4 5; do echo $i;sleep 1; 
done'
kubectl delete job job1

# backoffLimit:
retry failed job, default of 6 times
each retry on a seperate pod