# Mounting of NFS Volume for Kubernetes

## Static NFS Deployment
Run the following commands:
`kubectl apply -f 1-NFS-PVC-storage-class.yml`

`kubectl apply -f 2-NFS-PVC-Claim.yml`

`kubectl apply -f 3-nginx-test.yml`

If the nginx container is stuck on pending, run this command on all the nodes (master ans worker):
`sudo apt-get install -y nfs-common`

`systemctl daemon-reload && systemctl restart kubelet` 