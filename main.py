# This is a sample Python script.
# +79955085370
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.sessions import StringSession
import os
from dotenv import load_dotenv

# Загрузка значений переменных окружения
os.environ.setdefault('YY', 'True')
if os.environ.get('YY') == 'True':
    print('Debug mode is on')
else:
    print('Debug mode is off')

print(os.environ.get('YY'))