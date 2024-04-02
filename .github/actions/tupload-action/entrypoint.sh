#! /bin/sh -l

docker run --rm --name tupload \                                                            16:15:35
-e TELEGRAM_BOT_TOKEN=$1\
-e TELEGRAM_USER_ID=$2 \
-v $3:/tmp/file \
masterj3y/tupload:0.0.1
