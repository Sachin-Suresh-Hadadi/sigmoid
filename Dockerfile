FROM python:3.8-slim-buster
WORKDIR /project
RUN apt-get update && apt-get install -y python3
COPY ./project/requirements.txt requirements.txt
RUN  pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python3", "./project/manage.py", "runserver", "0.0.0.0:8000"]