#!/bin/bash

# Install Docker
sudo apt-get remove -y docker docker-engine docker.io
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update -y 
apt-cache policy docker-ce

sudo apt-get install -y docker-ce
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker

# Run docker command without sudo
#sudo passwd ${USER}
sudo groupadd docker
sudo usermod -aG docker ${USER}
su - ${USER}
id -nG
#sudo usermod -aG docker username


# Working with Docker Images
docker run hello-world
docker search ubuntu
docker pull ubuntu
docker run ubuntu
docker images

# Running a Docker Container
docker run -it ubuntu
apt-get update -y


# Committing Changes in a Container to a Docker Image

exit


# When you commit an image, the new image is saved locally
docker commit -m "What did you do to the image" -a "Author" <container-id> <repo>/<new_image_name>

docker images
docker ps -a
docker ps -l
docker stop container-id

# Pushing Docker Images to a Docker Repository
sudo docker login -u docker-username
sudo docker push docker-username/docker-image-name