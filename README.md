# Microsoft Big Data Clusters

# Deployment proceedure
## Deploy Kubernetes
### Add the current machine to the hosts file
`echo $(hostname -i) $(hostname) | sudo tee -a /etc/hosts`
### Disable swapping on all devices
```
sudo sed -i "/ swap / s/^/#/" /etc/fstab
sudo swapoff -a
```
### Import the keys and register the repository for Kubernetes
```
sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo 'deb http://apt.kubernetes.io/ kubernetes-xenial main' | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
```
### Configure docker and Kubernetes prerequisites on the machine
```
KUBE_DPKG_VERSION=1.15.0-00 #or your other target K8s version, which should be at least 1.13.
sudo apt-get update && \
sudo apt-get install -y ebtables ethtool && \
sudo apt-get install -y docker.io && \
sudo apt-get install -y apt-transport-https && \
sudo apt-get install -y kubelet=$KUBE_DPKG_VERSION kubeadm=$KUBE_DPKG_VERSION kubectl=$KUBE_DPKG_VERSION && \
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash
```
### Set net.bridge.bridge-nf-call-iptables=1
```
. /etc/os-release
if [ "$VERSION_CODENAME" == "bionic" ]; then sudo modprobe br_netfilter; fi
sudo sysctl net.bridge.bridge-nf-call-iptables=1
```
### Initialize Kubernetes master (FOR MASTER ONLY)


## Add persistent storage
### Local Storage
### Mount NFS (Active/Static) 
## Install Azdata CLI

## Kubernetes commands
This section will contain useful commands for debugging and/or configuring cluster information. 

## Checking cluster information
`kubectl cluster-info`

## Checking resources 
`kubectl get <resource-name> [--namespace <namespace>]`

| Available resource names | Short form |
| ---- | ---- |
| pods | - |
| services | svc |
| namespaces | - |
| deployments | - |

### Node had taints that the pod didn't tolerate error when deploying to Kubernetes cluster
This usually occurs if you only boostrapped a cluster with a single master node. 
`kubectl taint nodes <node-name> node-role.kubernetes.io/master-`