
FROM ubuntu:latest
COPY . /app
WORKDIR /app
RUN apt -y update
RUN apt install -y python3
RUN apt install -y python3-pip 
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install requests
CMD ["python3" "./mainapp.py"]