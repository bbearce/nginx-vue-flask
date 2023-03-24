# use python container image
From ubuntu:22.10
# From python:3.6-stretch

# set the working directory of the image filesystem 
WORKDIR /flask

# copy current directory to the working directory 
ADD . /flask

# Install tools and python dependencies
RUN apt update -y;
RUN apt-get install vim -y;
RUN apt-get install python3-pip -y;
RUN pip install -r requirements.txt


# start the uWSGI
CMD ["uwsgi", "app.ini"]