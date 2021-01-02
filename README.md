# Machine-Learning-and-Statistics-Project-2020
My project submission for the Machine Learning and Statistics module at GMIT

# Docker

This repository contains a Dockerfile which will allow you to build a docker image on your own machine in order to run a version of this web service.

Docker is .....

Installing Docker on Windows: https://docs.docker.com/docker-for-windows/install/

# Virtual Environment 

This repository contains a server which should be run in a virtual environment.

## Instructions to create and run a virtual environment for the first time on your machine

#### The command to install a virtual environment on your machine for the first time is:

python -m venv venv

#### To activate the virtual environment: 

.\venv\Scripts\activate.bat

#### Install the required packages:

The required packages to run this web application are listed in a txt file called requirements.txt in this repository. 

Instill the packages in your virtual environment with the command:

pip install -r requirements.txt

#### Pip warning

I got the below message when I created a virtual environment on my machine.

WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.
You should consider upgrading via the 'c:\users\john\desktop\machine-learning-and-statistics-project-2020\venv\scripts\python.exe -m pip install --upgrade pip' command.

#### Run my server

To get the server I have written up and running in the virtual environment use the commands below

1. set FLASK_APP=server.py
2. python -m flask run

#### To exit the virtual environment:

deactivate