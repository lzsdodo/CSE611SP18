# Install and Config Ganglia

## File Description
```
/etc/gmond.conf                 # Gmond Configuration
/ect/gmetad.conf                # Gmetad Configuration
/var/lib/ganglia/rrds/          # RRD File Storage
/usr/share/ganglia/             # Web File
/etc/httpd/conf.d/ganglia.conf  # Ganglia's Web Conf File
```

## Commands
```
sudo vi /etc/ganglia/gmond.conf
sudo vi /ect/gmetad.conf

sudo service gmetad start
sudo service ganglia-monitor start
sudo /etc/init.d/apache2 start
```

## Configuration
- Server
    - `/etc/ganglia/gmetad.conf`
    
- Client
    - `/etc/ganglia/gmond.conf`

## Reference
- [Install Ganglia on Ubuntu 16.04 Server (Xenial Xerus)](http://www.ubuntugeek.com/install-ganglia-on-ubuntu-16-04-server-xenial-xerus.html)
- [Introduction to Ganglia on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/introduction-to-ganglia-on-ubuntu-14-04)
- [How to Install and Configure Ganglia Monitor on Ubuntu 16.04](https://hostpresto.com/community/tutorials/how-to-install-and-configure-ganglia-monitor-on-ubuntu-16-04/)
- [Ganglia 监控工具简介与部署](https://blog.yangx.site/2016/06/23/ganglia-monitoring-tool/)