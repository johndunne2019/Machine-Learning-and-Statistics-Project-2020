# Machine-Learning-and-Statistics-Project-2020
My project submission for the Machine Learning and Statistics module at GMIT

Author - John Dunne G00273895

## About this Repository

This repository contains the resources required to run a web service that uses machine learning to make predictions based on the data in the power production data set. Further details on the contents of this repository can be seen in the next section below.

## Contents of this Repository

I have listed below the contents of this repository and a short description on each:

**Project-Machine-Learning-Statistics.ipynb**

Jupyter notebook containing among other things:

* An introduction to the power production data set.
* An introduction to artificial neural networks.
* Training a Keras neural network.
* Making predictions on unseen data with the neural network.
* Analysing the accuracy of the predictions.

**model.h5**

Keras neural network model saved with model.save command in jupyter notebook.

**server.py**

Python file that runs a flask server which serves out the predictions from the neural network at a specified app route on the web browser at local host.

**static**

Folder containing index.html which is the user front end for my API. Ajax function returns the prediction to the index.html from the app route specified in server.py

**img**

Folder containing images that are displayed in the jupyter notebook.

**.gitignore**

Contents of the file are ignored by Github.

**requirements.txt**

List of required packages needed to run this application. I compiled the list from a virtual environment using the command pip freeze > requirements.txt

**Dockerfile**

**.dockerignore**




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

Docker is .....

Installing Docker on Windows: https://docs.docker.com/docker-for-windows/install/

## requirements.txt

The requirements to run this project are listed in a requirements.txt file in my repository. 

I created a virtual environment and installed the required packages below:

* pip install flask
* pip install numpy
* pip install tensorflow or conda install tensorflow if this fails
* pip install -U scikit-learn

The command - pip install -r requirements.txt - can be used to install all required packages in a virtual environment on your own local machine.

## Virtual Environment 

This repository contains a server which should be run in a virtual environment.

Error importing tensorflow have to investigate further.

ImportError: DLL load failed while importing _pywrap_tensorflow_internal: A dynamic link library (DLL) initialization routine failed.

conda install tensorflow solves the issue  - https://stackoverflow.com/questions/49932993/importerror-dll-load-failed-a-dynamic-link-library-dll-initialization-routin

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