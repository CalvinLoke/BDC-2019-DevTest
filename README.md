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

```
cat <<EOF > rbac.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: default-rbac
subjects:
- kind: ServiceAccount
  name: default
  namespace: default
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
EOF
```

```
KUBE_VERSION=1.15.0
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --kubernetes-version=$KUBE_VERSION
```

```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

```
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
helm init
kubectl apply -f rbac.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/recommended/kubernetes-dashboard.yaml
kubectl create clusterrolebinding kubernetes-dashboard --clusterrole=cluster-admin --serviceaccount=kube-system:kubernetes-dashboard
```

`sudo kubeadm token create --print-join-command`

## Add persistent storage

### Local Storage

#### Run on all nodes

`git clone https://github.com/Calvinloke/BDC-2019-DevTest`

#### Run on Worker nodes only!

`cd BDC-2019-DevTest/KubernetesConfigurationFiles/Local-Storage`

`chmod +x setup-volumes-agent.sh`

`sudo ./setup-volumes-agent.sh`

#### Run on Master node only!

`kubectl apply -f local-storage.yml`

### Mount NFS (Active/Static) NOTE THAT THIS DOESN'T SEEM TO WORK AS OF DEC 2020 MAY UPDATE IF FOUND SOLUTION

<PLACEHOLDER>

## Install Azdata CLI (install on master node only or machine used to access the K8s cluster)

### Installation using apt

#### Install dependencies

```
sudo apt-get update
sudo apt-get install gnupg ca-certificates curl wget software-properties-common apt-transport-https lsb-release -y
```

#### Import microsoft key

```
curl -sL https://packages.microsoft.com/keys/microsoft.asc |
gpg --dearmor |
sudo tee /etc/apt/trusted.gpg.d/microsoft.asc.gpg > /dev/null
```

#### Create local repository

Ubuntu 16.04:

`sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/16.04/prod.list)"`

Ubuntu 18.04:

`sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/18.04/prod.list)"`

Ubuntu 20.04:

`sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/prod.list)"`

#### Install 

```
sudo apt-get update
sudo apt-get install -y azdata-cli
```

#### Verify install

```
azdata 
azdata --version
```

## Deploy BDC

NOTE THAT AS OF DEC 2020 I WAS NOT ABLE TO GET PERSISTENT STORAGE WITH NFS WORKING FOR BIG DATA CLUSTERS. 

### Run start command

`azdata bdc create --accept-eula=y`

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

### Getting join command for Kubernetes
`sudo kubeadm token create --print-join-command`

### Node had taints that the pod didn't tolerate error when deploying to Kubernetes cluster
This usually occurs if you only boostrapped a cluster with a single master node. 

`kubectl taint nodes <node-name> node-role.kubernetes.io/master-`

### Active directory (temp)

`export DOMAIN_SERVICE_ACCOUNT_USERNAME=contoso\administrator`

`export DOMAIN_SERVICE_ACCOUNT_PASSWORD=Password1`

`azdata bdc config replace -c custom-prod-kubeadm/control.json -j "$.security.activeDirectory.ouDistinguishedName=OU\=bdc\,DC\=contoso\,DC\=com"`

`azdata bdc config replace -c custom-prod-kubeadm/control.json -j "$.security.activeDirectory.dnsIpAddresses=[\"10.10.2.227\"]" `

`azdata bdc config replace -c custom-prod-kubeadm/control.json -j "$.security.activeDirectory.domainControllerFullyQualifiedDns=[\"AD2019.CONTOSO.com\"]" `

`azdata bdc config replace -c custom-prod-kubeadm/control.json -j "$.security.activeDirectory.clusterAdmins=[\"bdcadminsgroup\"]"`

`azdata bdc config replace -c custom-prod-kubeadm/control.json -j "$.security.activeDirectory.clusterUsers=[\"bdcusersgroup\"]"`