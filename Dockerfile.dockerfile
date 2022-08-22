FROM python:3.10
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD [ "gunicorn", "twitch_preserve.asgi:application", "-k","uvicorn.workers.UvicornWorker","--bind","0.0.0.0:8000" ]