FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
COPY external.conf /etc/nginx/conf.d/external.conf
RUN pip install -r /app/requirements.txt