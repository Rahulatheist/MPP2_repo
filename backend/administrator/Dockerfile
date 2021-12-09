FROM python:3.7-alpine
RUN apk add mariadb-dev
RUN apk add build-base
COPY . /administrator
WORKDIR /administrator
RUN echo Installing Python packages listed in requirements.txt
RUN pip install -r ./administrator/requirements.txt
EXPOSE 80
RUN echo Starting python and starting the Flask service...
ENTRYPOINT ["python"]
CMD ["administrator.py"]
