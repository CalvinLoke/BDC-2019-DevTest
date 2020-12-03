# Microsoft Big Data Clusters

# Deployment proceedure
## Deploy Kubernetes
## Mount NFS (Active/Static)
## Install Azdata CLI

## Kubernetes debugging commands
This section will contain the common errors and issues that I have encountered during the development testing period. 
### Node had taints that the pod didn't tolerate error when deploying to Kubernetes cluster
This usually occurs if you only boostrapped a cluster with a single master node. 
`kubectl taint nodes <node-name> node-role.kubernetes.io/master-`