# Instance Info on GCP

- Instance in GCP:
	- Name: `ann`, `bob`, `cindy`, `dan`		
	- Zone: `us-east1-b`      
	- Machine type: `2 vCPUs - 7.5 GB memory`     
	- OS Images: `Ubuntu 16.04 LTS` - `Standard persistent disk - 10GB`     

- Role:		
	- `ann` as the Ganglia Master			
	- `bob` runs the app on `TensorFlow`		
	- `cindy` runs the app on `Spark`		
	- `dan` runs the app on `MXNet`		

- Connect
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "ann"`     	 
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "bob"` 	
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "cindy"` 		
	- `gcloud compute --project "ub-cse-611" ssh --zone "us-east1-b" "dan"` 		


# Physical Machines
- Instance in CSE		
	- Name: `boulton`, `carnegie`, `edison` 			  	
