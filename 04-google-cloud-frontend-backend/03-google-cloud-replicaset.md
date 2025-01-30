# Google Cloud Frontend and Backend


## 1. Create backend


```
# Go to backend dir
cd 04-google-cloud-frontend-backend\backend-api

# Build image
gcloud builds submit --region=europe-north1 --tag europe-north1-docker.pkg.dev/sindre-dev-439512/docker-repo/backend-api . --project=sindre-dev-439512

# Deploy backend
kubectl apply -f kube-manifest/

# Get the Cluster IP of backend-api
kubectl get all

# The workload can be viewed here:
https://console.cloud.google.com/kubernetes/workload/overview?project=sindre-dev-439512
```


## 2. Deploy Frontend



```
# Go to backend dir
cd 04-google-cloud-frontend-backend\frontend-next

# Build image
gcloud builds submit --region=europe-north1 --tag europe-north1-docker.pkg.dev/sindre-dev-439512/docker-repo/frontend-next . --project=sindre-dev-439512

# Deploy backend
kubectl apply -f kube-manifest/

# Get the Cluster IP of backend-api
kubectl get all

# The workload can be viewed here:
https://console.cloud.google.com/kubernetes/workload/overview?project=sindre-dev-439512
```
