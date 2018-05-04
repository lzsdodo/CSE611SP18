# Instance Info on GCP

- Instance in GCP:
    - Name: `master`, `ann`, `bob`, `cindy`, 
    - Zone: `us-east1-b`      
    - Machine type: `2 vCPUs - 16 GB memory`     
    - OS Images: `Ubuntu 16.04 LTS` - `SSD - 25GB`	

- Role:		
    - `master` as the Ganglia Master
    - `ann`runs the app on `TensorFlow`
    - `bob` runs the app on `MXNet`
    - `cindy` runs the app on `Spark`

- Connect
    - `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "master"` 
    - `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "ann"`     	 
    - `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "bob"` 	
    - `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "cindy"` 		

- Data Collect
    - On "master": `/var/lib/ganglia/rrds/`

- Transfer local file to GCloud
    - `gcloud compute scp [LOCAL_FILE_PATH] [INSTANCE_NAME]:~/`
    - `gcloud compute scp [INSTANCE_NAME]:[REMOTE_FILE_PATH] [LOCAL_FILE_PATH]`

# Physical Machines
- Instance in CSE		
    - Name: `boulton`, `carnegie`, `edison`
