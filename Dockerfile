FROM python:alpine3.19

ADD main.py .

RUN pip install python-telegram-bot --upgrade

ENTRYPOINT ["python", "main.py"]
