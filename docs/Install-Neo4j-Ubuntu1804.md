# Install Nebula Graph database on Ubuntu 18.04

In thi document, you will learn how to install Nebula Graph step by step on Ubuntu 18.04. In fact, Dgraph be deployed directly on Linux, Windows. It can also running in Docker on Kubernetes. To run on K8s, it needs mount persist volumn to save data. This document will introduce both way.

## Install step by step

1. Install JDK. Neo4j written by Java, it needs to install OpenJDK on operation system. 

```shell
sudo apt-get update
sudo apt-get install openjdk-8-jdk
```

To check Java version, please use below command:

```shell
java -version
```

2. Deploy GPG key of Neo4j.

```shell
wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.org/repo stable/' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt-get update
```

3. Install Neo4j

```shell
sudo apt-get install neo4j
```

4. Install client

```shell
sudo add-apt-repository ppa:cleishm/neo4j
sudo apt-get update
sudo apt-get install neo4j-client libneo4j-client-dev
```