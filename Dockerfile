FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir flask pandas waitress

COPY . .
EXPOSE 5000

CMD python main.py