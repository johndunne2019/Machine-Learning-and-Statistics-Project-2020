# Docker file to create a docker image and run a docker container 
# John Dunne G00273895
# Adpated from example rando-app repo from lecture series - https://github.com/ianmcloughlin/random-app
# Changed python to exact version after readin forum post- https://learnonline.gmit.ie/mod/forum/discuss.php?d=12322

FROM python:3.8.5

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=server.py

CMD flask run --host=0.0.0.0