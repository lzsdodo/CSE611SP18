# Install and Config Ganglia


### Server
	
	```bash
	sudo vi /etc/ganglia/gmetad.conf
	sudo vi /etc/ganglia/gmond.conf

	sudo /etc/init.d/ganglia-monitor restart
	sudo /etc/init.d/gmetad restart
	sudo /etc/init.d/apache2 restart
	```
	
	```bash
	# gmetad.conf
	gridname "MyGrid"
	data_source "msproj" 5 35.196.96.186
	xml_port 8651
	interactive_port 8652
	setuid_username "nobody"
	rrd_rootdir "/var/lib/ganglia/rrds/"
	```
	
	```bash
	# gmond.conf
	globals {
		#...
		send_metadata_interval = 10
	}
	
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
- [Ganglia 监控工具简介与部署](https://blog.yangx.site/2016/06/23/ganglia-monitoring-tool/)