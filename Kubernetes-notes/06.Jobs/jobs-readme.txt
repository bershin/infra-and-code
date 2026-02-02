Job create a pod to execute a task.(Log analysis)
Usecase:
- Batch processing: ETL Jobs, Log analysis & report generation.
- Parallel processing: parallizing data analysis & image processing

============ restartPolicy: Never:
- Do not restart containers after they exit.

kubectl apply -f .
kubectl get job
kubectl get cronjob/cj
kubectl describe jobs
kubectl get pod
kubectl logs job1-ddr5q


kubectl create job job1 --image=alpine -- sh -c 'for i in 1 2 3 4 5; do echo $i;sleep 1; 
done'
kubectl delete job job1
============ backoffLimit:
Tell the job to retry number of times before marking the job as failed.
- each retry on a seperate pod
- default of 6 times
========== job completion
how many successful pods to be run for a job.
========== job Parallel
how many pods can run in parallel for a job, based on completion
========== job activedeadlinesecond
terminate the job, if it runs above the activedeadlinesecond limit
- try with less second and more second than sleep. 5/50