FROM python:3.8.18

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh

RUN chmod +x /usr/local/bin/wait-for-it.sh

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

WORKDIR /code