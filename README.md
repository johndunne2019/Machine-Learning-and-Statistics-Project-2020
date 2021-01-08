# Machine-Learning-and-Statistics-Project-2020
My project submission for the Machine Learning and Statistics module at GMIT

Author - John Dunne G00273895

## About this Repository

This repository contains the resources required to run a web service that uses machine learning to make predictions based on the data in the power production data set. Further details on the contents of this repository can be seen in the next section below.

## Running this web service on your local machine - quick start guide

A quick start guide to getting this web application up and running on your local machine.

I have included further details on each component later in this Readme file. 

1. Pull the latest version of my repository from Github.
2. Navigate to the folder on your local machine.
3. set FLASK_APP=server.py
4. python -m flask run
5. When server is running open local host in your web browser at - http://127.0.0.1:5000/
6. Enter your wind speed and click the Predict Power Output button to receive power output prediction.
7. When you are finished close the local host and Ctrl + C on your command line to kill the web server.

## Building a Docker Image and running a container - quick start guide

Further detailed instructions later in this Readme file.

1. Pull the latest version of the repository from Github.
2. Navigate to the folder on your local machine.
3. If you have docker installed you can check your version with the command - docker --version
4. docker build -t predictions-app to build a docker image (this may take a while).
5. docker image ls to see the image once it is built.
6. docker run -d -p 5000:5000 predictions-app to get a container running your local host.
7. Go to http://127.0.0.1:5000/ to see the web app. 
8. docker container ls - To see details on a container including the container ID.
9. docker kill container ID - To kill a docker container
9. docker container ls - to see all containers currently running.

## Contents of this Repository

I have listed below the contents of this repository and a short description on each:

#### Project-Machine-Learning-Statistics.ipynb

Jupyter notebook containing among other things:

* An introduction to the power production data set.
* An introduction to artificial neural networks.
* Training a Keras neural network.
* Making predictions on unseen data with the neural network.
* Analysing the accuracy of the predictions.

#### model.h5

Keras neural network model saved with model.save command in jupyter notebook.

#### server.py

Python file that runs a flask server which serves out the predictions from the neural network at a specified app route on the web browser at local host.

**static**

Folder containing index.html which is the user front end for my API. Ajax function returns the prediction to the index.html from the app route specified in server.py

#### img

Folder containing images that are displayed in the jupyter notebook.

#### .gitignore

Contents of the file are ignored by Github.

#### requirements.txt

List of required packages needed to run this application. I compiled the list from a virtual environment using the command pip freeze > requirements.txt

#### Dockerfile

File containing the commands to build a docker image of the web service in this repository.

#### .dockerignore

Contents of this file are ignored by Docker.

## Difficulty displaying jupyter notebook on Github website

Sometimes jupyter notebooks do not load on the Github website. If this happens you can copy and paste the URL of the notebook and paste in the below website which will display the notebook: https://nbviewer.jupyter.org/

I have included the URL of my Tasks.ipynb notebook here also for convenience: https://github.com/johndunne2019/Tasks-2020-Machine-Learning-and-Statistics/blob/main/Tasks.ipynb

## How to download this repository

1. Go to GitHub.
2. Go to my repository: https://github.com/johndunne2019/Fundamentals-of-Data-Analysis-Project-2019
3. Click the Code button which is colored green.
4. Click on HTTPS and copy the link that is shown.
5. Open the command line on your machine, navigate to the directory where you would like to clone the repository down to.
6. Enter the command: git clone followed by the URL of the repository.
7. The repository will be cloned down to your current working directory.
8. You will need to navigate to this folder location on the command line in order to run the program.
9. Details on how to view my jupyter notebook are described in the next section below.

## How to run the jupyter notebook

1. On the command line navigate to the folder location where the repository has been downloaded and saved to using the cd change directory command.
2. Type jupyter notebook on the command line and press enter
3. After a short wait jupyter notebook will open in your web browser.
4. Open the Tasks.ipynb notebook in the browser and the notebook containing the code and comments that I wrote for this assignment will be displayed.
5. If you want to run the code in any cell hold down the shift key and press enter and the command will run and the output wil be displayed in the next cell.
6. To change between edit and read mode at any time press the ESC key.
7. If you wish t run the entire notebook click Kernel in the toolbar at the top of the screen and then click Resstart and run all. The notebook will refresh and all code cells will be executed from top to bottom.
When you have finished viewing the jupyter notebook close the web browser and return to the command line. Press Ctrl + C on the command line to kill the program.

## Docker

This repository contains a Dockerfile which will allow you to build a docker image on your own machine in order to run a version of this web service.

Check you have Docker installed by running the below on your command line:

* docker --version

![dockerversion](/img/Docker--version.PNG)

If Docker is not installed visit:

* Installing Docker on Windows: https://docs.docker.com/docker-for-windows/install/

**Building a Docker Image**

A docker image is a template from which a docker container can be built.

To build a docker image in this repository navigate to the folder location on command line and type:

* docker build -t predictions-app .

![dockerbuild](/img/DockerBuildImage.PNG)

I have given the container an ID here before the final dot 

To see the docker image that has been built:

* docker image ls

![dockerimagels](/img/DockerImagels.PNG)

**Running a docker container**

A container is an instance of a docker image.

To get a container running on your machine:

* docker run -d -p 5000:5000 predictions-app

-d tells docker to run in the background.

-p 5000 - port 5000 will run on the linux machine and your own machine at the same time.

![dockerrun](/img/DockerRun.PNG)

**other commands**

* To see all containers by their ID: docker container ls

* To kill a container: docker kill container ID

* Delete a container: docker rm container ID

## requirements.txt

The requirements to run this project are listed in a requirements.txt file in my repository. 

I created a virtual environment and installed the required packages below:

* pip install flask
* pip install numpy
* pip install tensorflow or conda install tensorflow if this fails
* pip install -U scikit-learn

The command - pip install -r requirements.txt - can be used to install all required packages in a virtual environment on your own local machine.

## Virtual Environment 

I created a virtual environment on my machine. In this virtual environment I installed the required packages for running this repository and populated the requirements.txt file with the command pip freeze > requirements.txt. 

I added the venv to my .gitignore file so it would not be pushed to Github.

### Instructions to create and run a virtual environment for the first time on your machine

I have included below the instructions to create a venv and get it up and running on your local machine.

#### The command to install a virtual environment on your machine for the first time is:

* python -m venv venv

#### To activate the virtual environment: 

* .\venv\Scripts\activate.bat

#### Install the required packages:

The required packages to run this web application are listed in a txt file called requirements.txt in this repository. 

Instill the packages in your virtual environment with the command:

* pip install -r requirements.txt

#### Pip warning

I got the below message when I created a virtual environment on my machine.

WARNING: You are using pip version 20.1.1; however, version 20.3.3 is available.
You should consider upgrading via the 'c:\users\john\desktop\machine-learning-and-statistics-project-2020\venv\scripts\python.exe -m pip install --upgrade pip' command.

To check your current version of pip :

* pip --version

To upgrade pip on your machine

* python -m pip install --upgrade pip

#### Run my server

To get the server I have written up and running in the virtual environment use the commands below

1. set FLASK_APP=server.py
2. python -m flask run

#### To exit the virtual environment:

deactivate

## Image of web service up and running

![webapp1](/img/WebApp1.PNG)

![webapp2](/img/WebApp2.PNG)