# Datalakes
This repository serves as a continuation of both LearningWithK8s and LearningWithDocker. 

## Pre-requisites
Before attempting this deployment, ensure that you have provisioned Virtual Machines for the following:

- 1 for MongoDB
- 1 for SQL Server
- 1 for Microsoft Big Data Cluster

### Install Docker (Run on machines NOT part of the Main Big Data Cluster)
``` 
    sudo apt-get update && sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    sudo apt-get update
    
    sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### Give current user super user privileges 
`sudo groupadd docker`

`sudo usermod -aG docker $USER`

### Verify that Docker is installed

`sudo docker run hello-world`

### Pulling this repository 

`git clone https://github.com/CalvinLoke/Datalakes`

## Deploying MongoDB (Run this code on the machine that you wish to install MongoDB on)
Ensure that the machine running MongoDB has the following requirements:
- Storage
- Memory: 1GB 

### Deploying MongoDB 
`docker-compose -f mongodb-docker-compose.yml up`

Note that if you would like to run the containers in detached mode, add the `-d` flag to the command as follows:

`docker-compose -f mongodb-docker-compose.yml up -d`

The MongoDB service can now be accessed through port 27017. 

## Deploying SQL Server
<Insert system requirements for SQL Server here>

### Deploying SQL Server
`docker-compose -f sql-server-docker-compose.yml up`

`docker-compose -f sql-server-docker-compose.yml up -d`

The SQL Server service can now be accessed through port 1430. 
