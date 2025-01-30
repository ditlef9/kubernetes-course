# 05-google-cloud-private-cluster

## 1 Create Standard Private Cluster

Google Cloud > Kubernetes Engine > Clusters > `Create`

* Cluster Mode: Standard

Networking:

* Network access:
  * Private Cluster
  * [v] Access control plane using its external IP address
  * [v] Enable Control plane global access
  * Control plane IP range: 172.16.0.0/28
* [v] Enable Dataplane V2

Security
* [v] Enable Workload Identity

Features
* [v] Enable Compute Engine Persistent Disk CSI Driver
* [v] Enable Filestore CSI Driver

## 2 Create Cloud NAT gateway

Google Cloud > Network services > Cloud NAT

