FROM python:3.6

ENV CONATINER_HOME=/var/www

ADD . ${CONATINER_HOME}
WORKDIR ${CONATINER_HOME}

RUN pip install -r ${CONATINER_HOME}/requirements.txt