FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

ADD ./requirements/dev.txt /app/requirements/dev.txt
RUN pip install --no-cache-dir -r /app/requirements/dev.txt

COPY . ./

CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 -k sync main:app