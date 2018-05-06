# Ganglia

## File Description
- Ganglia Files

    ```
    /etc/ganglia/gmond.conf            # Gmond Configuration
    /ect/ganglia/gmetad.conf           # Gmetad Configuration
    /etc/ganglia/conf.d                # Ganglia Modules Configuration
    /usr/lib/ganglia/                  # C Modules
    /usr/lib/ganglia/python_modules/   # Python Scripts
    /var/lib/ganglia/rrds/             # RRD File Storage

    ```

- Web Files
    ```
    /etc/hosts                         # IP Hostname Maps
    /usr/share/ganglia/                # Web File
    /etc/httpd/conf.d/ganglia.conf     # Ganglia's Web Conf File
    ```

- Log Files
    ```
    /tmp/gmond.log
    /var/log/apache2/error_logs
    ```

## Data Collecting

    ```
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