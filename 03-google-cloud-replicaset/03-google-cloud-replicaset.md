# Google Cloud Replicaset


We will change `deployment.yml` to include `replicas: 3`:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: finnreka-gke
spec:
  replicas: 1
  selector:
    matchLabels:
      app: finnreka
  template:
    metadata:
      labels:
        app: finnreka
    spec:
      containers:
      - name: finnreka-app
        # Replace $LOCATION with your Artifact Registry location (e.g., us-west1).
        # Replace $GCLOUD_PROJECT with your project ID.
        image: europe-north1-docker.pkg.dev/sindre-dev-439512/docker-repo/finnreka-gke:latest
        # This app listens on port 8080 for web traffic by default.
        ports:
        - containerPort: 8080
        env:
          - name: PORT
            value: "8080"
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
            ephemeral-storage: "1Gi"
          limits:
            memory: "1Gi"
            cpu: "500m"
            ephemeral-storage: "1Gi"
```