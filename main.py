import asyncio
import sys
import logging
import argparse
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

arg_parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="this program sends a file using telegram"
)

arg_parser.add_argument(
    '-t', '--token', metavar='TOKEN', help='Bot token'
)

arg_parser.add_argument(
    '-f', '--file', metavar='FILE', help='Path to the file'
)

arg_parser.add_argument(
    '-u', '--user', metavar='USER', help='User(numeric) ID'
)

args = vars(arg_parser.parse_args())

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot_token = args['token']
user_id = args['user']
file_path = args['file']

if not bot_token:
    logging.error("Bot token must be specified using -t argument")
    sys.exit(1)

if not user_id:
    logging.error("User id must be specified using -u argument")
    sys.exit(2)

if not file_path:
    logging.error("File path must be specified using -f argument")
    sys.exit(3)

application = ApplicationBuilder().token(bot_token).build()
bot = application.bot

file = open(file_path, 'rb')
asyncio.run(
    bot.send_document(
        chat_id=user_id,
        document=file
    )
)
