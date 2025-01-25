
## GKE Standard Cluster vs Autopilot Cluster

GKE Standard Cluster:
* Noded are user maintaned and operates

GKE Autopilot Cluster:
* Nodes are GKE provisioned, maintained and operated


## Create a  Cluster

1. Either a Standard Cluster or Autopilot Cluster:

Google Cloud Console > Kubernetes Engine > Clusters > `New`.

Cluster basics
* Name: cluster-1
* Region: europe-north1
* Cluster tier: Standard tier

Click `Create cluster`


## Commands

Connect to the cluster - Command-line access

Click on the three dots right to the cluster and select `Connect`:

**Connect:**<br>
`gcloud container clusters get-credentials cluster-1 --region europe-north1 --project sindre-dev-439512`

Output:
```commandline
Fetching cluster endpoint and auth data.
kubeconfig entry generated for cluster-1.
```

**See version:**<br>
`kubectl version`

Output:
```commandline
Client Version: v1.29.2
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
Server Version: v1.31.4-gke.1183000
WARNING: version difference between client (1.29) and server (1.31) exceeds the supported minor version skew of +/-1
```

**Get nodes:**<br>

`kubectl get nodes`

**Get pods:**<br>

`kubectl get pods`


## Deploy sample application

```
cd 01-google-cloud-kubernetes\deploy-sample-application
```

**Build and Push Docker Image to Artifact Registry**<br >

Start `Docker Desktop`.

*Create a Docker repository in Artifact Registry:*<br>

```commandline
gcloud artifacts repositories create docker-repo --repository-format=docker --location=europe-north1 --description="Docker repository"
gcloud artifacts repositories list
```

The artifact registry repository should be available here:
https://console.cloud.google.com/artifacts?project=sindre-dev-439512



```
gcloud builds submit --region=europe-north1 --tag europe-north1-docker.pkg.dev/sindre-dev-439512/docker-repo/finnreka-gke .
```

**List images:**<br>

```
gcloud artifacts repositories list
gcloud artifacts docker images list europe-north1-docker.pkg.dev/sindre-dev-439512/finnreka-repo

```

**Deploy:**<br>
```
kubectl apply -f kube-manifest/
```

**Get deployment:**<br>
```
kubectl get deployment
kubectl get service
```

