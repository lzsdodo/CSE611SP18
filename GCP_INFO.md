# Instance Info on GCP

- Instance in GCP:
	- Name: `ann`, `bob`, `cindy`, `ganglia`		
	- Zone: `us-east1-b`      
	- Machine type: `2 vCPUs - 8 GB memory`     
	- OS Images: `Ubuntu 16.04 LTS` - `SSD - 20GB`     

- Role:		
	- `ann`runs the app on `TensorFlow`
	- `bob` runs the app on `MXNet`
	- `cindy` runs the app on `Spark`
	- `ganglia` as the Ganglia Master

- Connect
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "ann"`     	 
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "bob"` 	
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "cindy"` 		
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "ganglia"` 		

- Data Collect
	- `/var/lib/ganglia/rrds/`

- Command
	- `gcloud compute scp [LOCAL_FILE_PATH] [INSTANCE_NAME]:~/`
	- `gcloud compute scp [INSTANCE_NAME]:[REMOTE_FILE_PATH] [LOCAL_FILE_PATH]`

# Physical Machines
- Instance in CSE		
	- Name: `boulton`, `carnegie`, `edison` 			  	
