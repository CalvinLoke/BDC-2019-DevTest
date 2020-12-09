# Mounting of NFS Volume for Kubernetes

## Installing the NFS Server

Create local directory

`sudo mkdir /srv/nfs/kubedata -p`

Change ownership 

`sudo chown -R nobody:nogroup /srv/nfs/kubedata`

Change read write permissions

`sudo chmod 777 /srv/nfs/kubedata`

Install NFS Kernel

`sudo apt install nfs-kernel-server nfs-common`

Change ownership 

`sudo chown nfsnobody: /srv/nfs/kubedata/`

Enable, start and check status

```
sudo systemctl enable nfs-server
sudo systemctl start nfs-server
sudo systemctl status nfs-server
```

Edit exports file

```
sudo vi /etc/exports
/srv/nfs/kubedata *
(rw,sync,no_subtree_check,no_root_squash,no_all_squash,insecure)
```

Run exportfs command

`sudo exportfs -rv`

`showmount -e`

## Setting up master and worker nodes

`sudo apt-get install -y nfs-common`

Mounting of NFS directory

`sudo mount -t nfs <ip-address>:/srv/nfs/kubedata /mnt`

Mount validation

`mount | grep kubedata`

## Static NFS Deployment
Run the following commands:

`kubectl apply -f 1-NFS-PVC-storage-class.yml`

`kubectl apply -f 2-NFS-PVC-Claim.yml`

`kubectl apply -f 3-nginx-test.yml`

## Dynamic NFS Provisioning

Run the following commands:

`kubectl apply -f 1-rbac-service-account.yml`

`kubectl apply -f 2-nfs-storage-class.yml`

`kubectl apply -f 3-nfs-client-provisioner.yml`

`kubectl apply -f 4-pv-claim.yml`

`kubectl apply -f 5-nginx-test-deployment.yml`

If the nginx container is stuck on pending, run this command on all the nodes (master ans worker):
`sudo apt-get install -y nfs-common`

`systemctl daemon-reload && systemctl restart kubelet` 