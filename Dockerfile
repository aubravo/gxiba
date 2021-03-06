FROM ubuntu:20.04

RUN mkdir -p /gxiba/src
COPY requirements.txt /gxiba/src



RUN apt-get update
RUN apt-get install python3-pip -y
RUN apt-get install python3 -y
RUN python3 -m pip install -r /gxiba/src/requirements.txt

WORKDIR /gxiba/src
COPY . /gxiba/src
RUN ln -s /usr/bin/python3.8 /usr/bin/python

CMD ["python", "-m", "luigi", "--module", "gxiba", "ImageQuery", "--platform", "SENTINEL", "--local-scheduler"]