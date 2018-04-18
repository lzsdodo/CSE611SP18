# Install and Config Ganglia

## Instruction
### Basic

	```bash
	sudo apt-get -y update && sudo apt-get -y upgrade
	# http://<master_node_ip>/ganglia
	
	# Install Gmond
	## Ubuntu
	sudo apt-get install -y ganglia-monitor
	## CentOS
	sudo yum install -y ganglia-gmond

	# Install Gmetad
	## Ubuntu
	sudo apt-get install -y gmetad
	## CentOS
	sudo yum install -y ganglia-gmetad
	```


### Server

	```bash
	# Installing LAMP Stack
	sudo apt-get install -y apache2 php libapache2-mod-php rrdtool
	
	sudo systemctl start apache2 
	sudo systemctl enable apache2
	
	# Install Ganglia Server
	sudo apt-get install -y ganglia-monitor gmetad ganglia-webfrontend
	```
	
	```bash
	# Configure Ganglia Master Node
	sudo cp /etc/ganglia-webfrontend/apache.conf /etc/apache2/sites-enabled/ganglia.conf
	sudo vi /etc/ganglia/gmetad.conf
	sudo vi /etc/ganglia/gmond.conf
	
	sudo /etc/init.d/ganglia-monitor restart
	sudo /etc/init.d/gmetad restart
	sudo /etc/init.d/apache2 restart
	```
	
	```bash
	# gmetad.conf
	data_source "msproj" 30 master:8649 client1:8649 client2:8649 #<master_ip>:8649 <client_ip:8649> ...
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
		host = 35.196.148.68 #<master_node_ip>
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
	sudo /etc/init.d/ganglia-monitor restart
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
		host = 35.196.148.68 #<master_node_ip>
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