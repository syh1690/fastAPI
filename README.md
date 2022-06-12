*****steps to run API locally******

source env/bin/activate   
#activates virtual environment

pip3 install -r requirements.txt
#installs all libraries in requirements.txt into virtual environment

uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
#runs API on local host

control + c
#stop the server on local API

deactivate
#deactivates virtual environment

###steps to build docker image and deploy###

docker build -t syh_api .
#builds docker image

docker run -d --name mycontainer -p 80:80 syh_api
#runs docker image locally

docker login
docker tag syh_api:latest syh1690/syh-api
docker push syh1690/syh-api:latest
#restart azure container instance to pull in new docker image