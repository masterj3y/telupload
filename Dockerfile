FROM python:alpine3.19

ADD main.py .

RUN pip install python-telegram-bot --upgrade

ENTRYPOINT python main.py -t "${TELEGRAM_BOT_TOKEN}" -u "${TELEGRAM_USER_ID}" -f /tmp/file
