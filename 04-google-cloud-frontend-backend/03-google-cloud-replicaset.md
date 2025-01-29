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



**Create image**
```
cd 03-google-cloud-replicaset/deploy-replicaset-app
gcloud builds submit --region=europe-north1 --tag europe-north1-docker.pkg.dev/sindre-dev-439512/docker-repo/hello . --project=sindre-dev-439512
```

**Deploy:**<br>
```
kubectl apply -f kube-manifest/
```

**Get deployment, service and replicaset:**<br>
```
kubectl get deployment
kubectl get service
kubectl get replicaset
kubectl get pods
kubectl describe pod <pod-name>
```


**Get deployment:**<br>
```
kubectl get pods
kubectl describe pod finnreka-gke-576dc5464d-kmw8m
```


**Connect to pod and exec commands to it:**<br>
```
kubectl exec -it finnreka-gke-576dc5464d-kmw8m

ls
hostname
```