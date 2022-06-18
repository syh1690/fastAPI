# Steps to run API locally

1. Activates virtual environment  

        source env/bin/activate  

2.  Installs all libraries in requirements.txt into virtual environment

        pip3 install -r requirements.txt

3. Runs API on local host

        uvicorn app.main:app --host 0.0.0.0 --port 80 --reload

4. Stop the server on local API

        control + c

5. Deactivates virtual environment

        deactivate

# Steps to build docker image and deploy

1. Builds docker image

        docker build -t syh_api .

2. Runs docker image locally

        docker run -d --name mycontainer -p 80:80 syh_api

#  steps to deploy to azure cloud
1. Run the commands in the terminal below

        docker login
        docker tag syh_api:latest syh1690/syh-api
        docker push syh1690/syh-api:latest

2. Restart azure container instance to pull in new docker image