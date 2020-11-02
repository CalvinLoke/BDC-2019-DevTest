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

## Noteable setbacks during deployment
This section will cover the different setbacks and difficulties I faced during the deployment of Big Data Clusters

### Non-relational databases
The schema of certain complex databases can/will result in long query times due to the resulting schema created (in the form of an external table on the BDC). Hence, one should take note of how the data is stored on the mon-relational database before using it as an external source. 

## Features of BDC
This section will contain some of my thoughts and evaluation of BDC and its capabilities. 

### Jupyter Notebooks
Jupyter Notebooks is now an integrated feature in Azure Data Studio, and provides a form of cross-platform compatibility for database management commands. It supports a wide variety of languages including SQL, Python and Spark. As compared to traditional SQL files, these can be shared with other Database Administrators that might be running on a different environment (eg Linux or MacOS). The notebooks are also generic in nature, in the sense that connections are managed based on where it is deployed, and its not shipped together with the notebook itself, thus eliminating the risk of a security breach due to the distribution of notebooks. 

Multiple Notebooks can be compiled together to form a *Jupytwer Book* which can serve as a reference file, that executes queries/commands to the SQL Server. 

#### Deploying clusters with Notebooks
The deployment of a Big Data Cluster can be done through the use of notebooks as well