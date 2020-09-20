# Install Nebula database on Ubuntu 18.04

In this document, You will learn how to install Nebula database on Ubuntu 18.04 manually and deploy Nebula docker on Kubernetes.

## Install Nebula step by step

1. Run commands below to install curl and apt-transport-https

``` shell
sudo apt update
sudo apt install curl apt-transport-https
```

2. Download package from nebula-graph.io website.
   
```shell
mkdir nebula
cd nebula
wget https://oss-cdn.nebula-graph.io/package/1.0.1/nebula-1.0.1.ubuntu1804.amd64.deb
```
To download packages for other Linux OS, please reference below:

```shell
Centos 6: https://oss-cdn.nebula-graph.io/package/1.0.1/nebula-1.0.1.el6-5.x86_64.rpm
Centos 7: https://oss-cdn.nebula-graph.io/package/1.0.1/nebula-1.0.1.el7-5.x86_64.rpm
Ubuntu 1604: https://oss-cdn.nebula-graph.io/package/1.0.1/nebula-1.0.1.ubuntu1604.amd64.deb
```

3. Install Nebula from package

```shell
sudo dpkg -i nebula-1.0.1.ubuntu1804.amd64.deb
```
if using CentOS or RHEL, please execute below:

```shell
sudo rpm -ivh nebula-1.0.1.el7-5.x86_64.rpm
```

4. Start Nebula services
Nebula service has a lot of steps to start. Nebula offers a script file to auto start service. The file located at /usr/local/bin/nebula/scripts/nebula.service

```shell
sudo /usr/local/nebula/scripts/nebula.service start all
```
To stop service:

```shell
sudo /usr/local/nebula/scripts/nebula.service stop all
```

To view service status:

```shell
sudo /usr/local/nebula/scripts/nebula.service status all
```

To gurantuee Nebula always start after Linux start/restart, you need to create a service configuration file and add to systemctl.

```shell
sudo nano /etc/systemd/system/nebula.service
```

And then copy/paste below content into service file, press Ctrl + X to save file and quit.

```shell
[Unit] 
Description=Run Nebula Service at Startup 
After=default.target 
 
[Service] 
ExecStart=/usr/local/nebula/scripts/nebula.service start all
 
[Install] 
WantedBy=default.target 
```
Add this service configuration file into systemctl.

```shell
sudo systemctl daemon-reload 
sudo systemctl enable nebula.service 
```

5. Service Listening Ports

Please enable 3699, 45500, 44500 on firewall and Network Security Group.

```shell

[INFO] nebula-metad: Running as 2576, Listening on 45500
[INFO] nebula-graphd: Running as 2603, Listening on 3699
[INFO] nebula-storaged: Running as 2652, Listening on 44500

```