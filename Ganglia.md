# Install and Config Ganglia

## Instruction
### Basic

	```bash
	sudo apt-get -y update 
	sudo apt-get -y upgrade
	
	# Configure Firewall
	sudo ufw enable
	sudo ufw allow 8649
	sudo ufw status
	
	# http://<master_node_ip>/ganglia
	```
	
### Server

	```bash
	# Installing LAMP Stack
	sudo apt-get install -y apache2 mariadb-server php7.0 libapache2-mod-php7.0 php7.0-mbstring php7.0-curl php7.0-zip php7.0-gd php7.0-mysql php7.0-curl php7.0-mcrypt
	
	sudo systemctl start apache2 
	sudo systemctl enable apache2
	
	# Install Ganglia Server
	sudo apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend
	```
	
	```bash
	# Configure Ganglia Master Node
	sudo cp /etc/ganglia-webfrontend/apache.conf /etc/apache2/sites-enabled/ganglia.conf
	
	sudo vi /etc/ganglia/gmetad.conf
	sudo vi /etc/ganglia/gmond.conf
	
	sudo systemctl restart ganglia-monitor 
	sudo systemctl restart gmetad 
	sudo systemctl restart apache2
	```
	
	```bash
	# gmetad.conf
	data_source "msproj" 60 <master_node_ip>:8649
	```
	
	```bash
	# gmond.conf
	cluster {
		name = "msproj"
		owner = "unspecified"
		latlong = "unspecified"
		url = "unspecified"
	}
	
	udp_send_channel {
		# mcast_join = 239.2.11.71
		host = <master_node_ip>
		port = 8649
		ttl = 1
	}
	
	udp_recv_channel {
		# mcast_join = 239.2.11.71
		port = 8649
		# bind = 239.2.11.71
	}
	
	tcp_accept_channel { 
		port = 8649 
	}
	```
	
### Client

	```bash
	# Install Ganglia Client
	sudo apt-get install -y ganglia-monitor
	```

	```bash
	# Configure Ganglia Client Node
	sudo vi /etc/ganglia/gmond.conf

	sudo systemctl start ganglia-monitor
	```

	```bash
	# gmond.conf
	cluster {
		name = "msproj"
		owner = "unspecified"
		latlong = "unspecified"
		url = "unspecified"
	}
	
	udp_send_channel {
		# mcast_join = 239.2.11.71
		host = <master_node_ip>
		port = 8649
		ttl = 1
	}
	
	#udp_recv_channel {
	#  mcast_join = 239.2.11.71
	#  port = 8649
	#  bind = 239.2.11.71
	#}

	tcp_accept_channel { 
		port = 8649 
	}
	```

## Reference
- [Install Ganglia on Ubuntu 16.04 Server (Xenial Xerus)](http://www.ubuntugeek.com/install-ganglia-on-ubuntu-16-04-server-xenial-xerus.html)
- [Introduction to Ganglia on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/introduction-to-ganglia-on-ubuntu-14-04)
- [How to Install and Configure Ganglia Monitor on Ubuntu 16.04](https://hostpresto.com/community/tutorials/how-to-install-and-configure-ganglia-monitor-on-ubuntu-16-04/)