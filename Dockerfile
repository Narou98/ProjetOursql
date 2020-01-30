#getting python image
FROM ubuntu:latest
FROM python:3
COPY *.py /

RUN apt -y update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask
RUN pip3 install flask-restful
RUN pip3 install requests

EXPOSE 8889

CMD ["python3", "./mainapp.py"]


