FROM python:3
MAINTAINER Michael J. Stealey

RUN apt-get update && \
    apt-get install -y python3-virtualenv && \
    /usr/local/bin/python -m pip install --upgrade pip

WORKDIR /
VOLUME /code
COPY ./app.py /code/app.py
COPY ./requirements.txt /requirements.txt
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["run_server"]
