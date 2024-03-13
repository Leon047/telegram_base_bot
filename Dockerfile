FROM python:3.11
WORKDIR /bot 
COPY . /bot
RUN apt-get update -y &&\
    	pip install --upgrade pip &&\
    	pip install --no-cache -r requirements.txt 
