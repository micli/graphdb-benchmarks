# Install Dgraph database on Ubuntu 18.04

In thi document, you will learn how to install Dgraph step by step on Ubuntu 18.04. In fact, Dgraph be deployed directly on Linux, Windows. It can also running in Docker on Kubernetes. To run on K8s, it needs mount persist volumn to save data. This document will introduce both way.


## Open firewall ports if use remotely

The Dgraph has a lot of communication ports to receive varity calls from client. To ensure Dgraph works correctly, it need to open inbound ports: 5080, 6080, 7080, 8080, 9080. To enable Web UI remotely, it also need to open inbound port 8000.

It is pre-requirements in both of virtual machine and Kubernetes.

## Install step by step Manually


1. Run commands below to install curl and apt-transport-https

``` shell
sudo apt update
sudo apt install curl apt-transport-https
```

2. Download and install Dgraph. It will automatically start to run install bash. By default, Dgraph will install to folder: /usr/local/bin/

```shell
curl https://get.dgraph.io -sSf | bash
```

3. Create a user and a user group, both of them named to dgraph

```shell
sudo groupadd --system dgraph
sudo useradd --system -d /var/run/dgraph -s /bin/false -g dgraph dgraph
```

4. Run the commands below to create directories for Dgraph logs and state files.

```shell
sudo mkdir -p /var/log/dgraph
sudo mkdir -p /var/run/dgraph/{p,w,zw}
sudo chown -R dgraph:dgraph /var/{run,log}/dgraph
```

5. Create a service configuration file to describ dgraph service.
   
```shell
sudo nano /etc/systemd/system/dgraph.service
```

And then copy/paste below content into service file, press Ctrl + X to save file and quit.

```shell
[Unit]
Description=dgraph.io data server
Wants=network.target
After=network.target dgraph-zero.service
Requires=dgraph-zero.service

[Service]
Type=simple
ExecStart=/usr/local/bin/dgraph alpha --lru_mb 2048 -p /var/run/dgraph/p -w /var/run/dgraph/w
StandardOutput=journal
StandardError=journal
User=dgraph
Group=dgraph

[Install]
WantedBy=multi-user.target
```

6. Create a service configuration file to describ dgraph-zero service.

```shell
sudo nano /etc/systemd/system/dgraph-zero.service
```
And then copy/paste below content into service file, press Ctrl + X to save file and quit.

```shell
[Unit]
Description=dgraph.io zero server
Wants=network.target
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/dgraph zero --wal /var/run/dgraph/zw
StandardOutput=journal
StandardError=journal
User=dgraph
Group=dgraph

[Install]
WantedBy=multi-user.target
RequiredBy=dgraph.service
```

7. Create a service configuration file to describ dgraph-ui service.

```shell
sudo nano /etc/systemd/system/dgraph-ui.service
```
And then copy/paste below content into service file, press Ctrl + X to save file and quit.

```shell
[Unit]
Description=dgraph.io UI server
Wants=network.target
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/dgraph-ratel
StandardOutput=journal
StandardError=journal
User=dgraph
Group=dgraph

[Install]
WantedBy=multi-user.target
```

8. Add services into systemctl and start immediately.

```shell
sudo systemctl daemon-reload
sudo systemctl enable --now dgraph
sudo systemctl enable --now dgraph-ui
```

9. Access Web UI by http://{ipaddress}:8000. At server connection UI, specify server http://{ipaddress}:8080. Login without user id and password.


## Data import

dgraph live -f 21million.rdf.gz --schema film.schema
