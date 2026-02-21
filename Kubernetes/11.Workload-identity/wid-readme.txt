Check workload identity is enabled & see ds - done
- kubectl get nodes --show-labels | grep gke-metadata-server-enabled=true
create a service account
- gcloud iam service-accounts create <gcp-sa> 
- gcloud iam service-accounts list
assign compute viewer role to it
- gcloud projects add-iam-policy-binding <proj-id> \
    --member="serviceAccount:<gcp-sa>@<proj-id>.iam.gserviceaccount.com" \
    --role="roles/compute.viewer"
- gcloud projects get-iam-policy <proj-id>


create namespace
# kubectl create ns <KNS>
# kubens <KNS>
create kubernetes service account
# kubectl create sa <KSA>
- add the policy
# gcloud iam service-accounts add-iam-policy-binding <<gcp-sa>@<proj-id>.iam.gserviceaccount.com \
 --member="serviceAccount:<Workload identity namespace>[<KNS>/<KSA>]" \
 --role="roles/iam.workloadIdentityUser"
# gcloud iam service-accounts get-iam-policy <gcp-sa>@<proj-id>.iam.gserviceaccount.com
- annotate the service account
# kubectl annotate sa <KSA> iam.gke.io/gcp-service-account=<gcp-sa>@<proj-id>.iam.gserviceaccount.com
create po with the servive account
check the permission by loggin into pod.


gcloud beta container \
    --project \
"project-f09e95b2-bc36-4b45-bf4" clusters create "bj-priv-clus-1" \
    --region \
"us-central1" \
    --machine-type \
"e2-small" \
    --image-type \
"COS_CONTAINERD" \
    --disk-type \
"pd-standard" \
    --disk-size \
"20" \
    --num-nodes \
"1" \
    --enable-private-nodes \
    --enable-ip-alias \
    --network \
"projects/project-f09e95b2-bc36-4b45-bf4/global/networks/default" \
    --subnetwork \
"projects/project-f09e95b2-bc36-4b45-bf4/regions/us-central1/subnetworks/default" \
    --workload-pool \
"project-f09e95b2-bc36-4b45-bf4.svc.id.goog" 

---
External DNS
helm repo add external-dns https://kubernetes-sigs.github.io/external-dns/

helm upgrade --install external-dns external-dns/external-dns \
> --set provider=google \
> --set policy=sync \
> --set google-zone-visibility=public \
> --set txt-owner-id=k8s \
> --set serviceAccount.create=false \
> --set serviceAccount.name=external-dns-ksa \
> -n external-dns-ns

helm list -n external-dns-ns