FROM python:3.7-alpine
RUN apk add mariadb-dev
RUN apk add build-base
WORKDIR /administrator_app
COPY * ./
RUN echo Installing Python packages listed in requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
RUN echo Starting python and starting the Flask service...
ENTRYPOINT ["python"]
CMD ["administrator.py"]
