# Ganglia

## File Description

- Ganglia Files

    ```bash
    /etc/ganglia/gmond.conf            # Gmond Configuration
    /ect/ganglia/gmetad.conf           # Gmetad Configuration
    /etc/ganglia/conf.d                # Ganglia Modules Configuration
    /usr/lib/ganglia/                  # C Modules
    /usr/lib/ganglia/python_modules/   # Python Scripts
    /var/lib/ganglia/rrds/             # RRD File Storage
    ```

- Web Files

    ```bash
    /etc/hosts                         # IP Hostname Maps
    /usr/share/ganglia/                # Ganglia Web File
    /etc/httpd/conf.d/ganglia.conf     # Ganglia Web Conf File
    /etc/httpd/conf.d/httpd.conf       # Httpd Config
    /var/www/html                      # Httpd Web File
    ```

- Log Files

    ```bash
    /tmp/gmond.log
    /var/log/apache2/error_logs
    ```

- Config

    ```bash
    include('/etc/ganglia/conf.d/*.conf')
    ```

## Data Collecting

```bash
load_one
load_five
load_fifteen

cpu_num
cpu_speed
cpu_intr
cpu_sintr
cpu_idle
cpu_aidle
cpu_nice
cpu_user
cpu_system
cpu_wio

disk_total
disk_free

mem_total
mem_cached
mem_free
mem_buffers
mem_shared

swap_total
swap_free

proc_run
proc_total

pkts_in
pkts_out
bytes_in
bytes_out
```

## Ganglia Web

- 查看监控界面
    - `http://ip/ganglia`
    - Hosts up: <数量是否与节点数相同>

- 命令行工具 `gstat`
    - `gstat -a`


## Configurate HBase

- 所有的 hadoop node 上，配置 `hadoop-metrics2.properties`
    - 注释掉原来的所有配置
    - 添加需要的配置

    ```sh
    *.sink.ganglia.class=org.apache.hadoop.metrics2.sink.ganglia.GangliaSink21
    *.sink.ganglia.period=10
    *.sink.ganglia.slope=jvm.metrics.gcCount=zero,jvm.metrics.memHeapUsedM=both
    *.sink.ganglia.dmax=jvm.metrics.threadsBlocked=70,jvm.metrics.memHeapUsedM=40

    namenode.sink.ganglia.servers=10.142.0.5:8649
    resourcemanager.sink.ganglia.servers=10.142.0.5:8649
    datanode.sink.ganglia.servers=10.142.0.5:8649
    nodemanager.sink.ganglia.servers=10.142.0.5:8649
    maptask.sink.ganglia.servers=10.142.0.5:8649
    reducetask.sink.ganglia.servers=10.142.0.5:8649
    ```

- 所有的 hadoop node 上，配置 `hadoop-metrics2-hbase.properties`
    - 注释掉原来的所有配置
    - 添加需要的配置

    ```sh
    *.sink.ganglia.class=org.apache.hadoop.metrics2.sink.ganglia.GangliaSink31
    *.sink.ganglia.period=10

    hbase.sink.ganglia.period=10
    hbase.sink.ganglia.servers=10.142.0.5:8649
    ```

- Restart

    ```
    cd hadoop-x.x.x/sbin
    ./start-all.sh
    cd hbase-x.x.x/bin
    ./start-hbase.sh
    ```
