# Microsoft Big Data Clusters

## Kubernetes debugging commands

### Node had taints that the pod didn't tolerate error when deploying to Kubernetes cluster
This usually occurs if you only boostrapped a cluster with a single master node. 
`kubectl taint nodes <node-name> node-role.kubernetes.io/master-`