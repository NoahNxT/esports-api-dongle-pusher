FROM python:3.9.5

COPY ./app /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD [ "python3", "dongle.py" ]
