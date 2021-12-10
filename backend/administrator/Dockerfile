FROM python:3.7-alpine
RUN apk add mariadb-dev
RUN apk add build-base
WORKDIR /administrator_app
COPY . /administrator_app/
RUN echo Installing Python packages listed in requirements.txt
RUN cat /administrator_app/requirements.txt
RUN pip install -r /administrator_app/requirements.txt
EXPOSE 80
RUN echo Starting python and starting the Flask service...
ENTRYPOINT ["python"]
CMD ["administrator.py"]
