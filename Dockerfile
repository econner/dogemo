FROM orchardup/python:2.7
RUN apt-get update -qq && apt-get install -y python-mysqldb
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/