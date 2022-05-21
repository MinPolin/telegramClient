import requests
import json
import time
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import functions,types
import flask
from flask import request

from dotenv import load_dotenv
app = flask.Flask(__name__)




dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
SESSION_STRING = os.environ.get('SESSION_STRING')

TIME_SLEEP=10

URL="https://broadcast-management-test.herokuapp.com/tg/"
Polina='MinPolin'
Vlad='whatislove_sakharov'

def get_data(url):
    response = requests.get(url)
    content = response.content.decode()
    data = json.loads(content)

    return data


def get_client():
    api_hash = API_HASH
    api_id = API_ID
    name = 'admin'
    return TelegramClient(StringSession(SESSION_STRING), api_id, api_hash)

client = get_client()

async def create_chat(username,title):
    await client(functions.messages.CreateChatRequest(username, title=title))

async def send_msg(username):
    # Now you can use all client methods listed below, like for example...
    await client.send_message(username, 'I will create a chat instead of this msg')

@app.route("/", methods=['GET', 'POST'])
def main():
    print('smth')
    print(request)
    # req
    # print(data['flag'])
    # if data['flag']:
    #     print(data['chat'])
    #     username=list(data['chat']['0']['part'].split(','))
    #     title=data['chat']['0']['name']
    #     with client:
    #         client.loop.run_until_complete(create_chat(username,title))
    # else:
    #     print('Waiting to the next command')
    # # keyy=input('keyy =\n')
    return {'data':'v'}


@app.route('/hello')
def hello():
    keyy = ''
    print('start')
    # while keyy!="q":
    for i in range(15):

        time.sleep(TIME_SLEEP)

        data = get_data(URL)
        print(data['flag'])
        if data['flag']:
            print(data['chat'])
            username = list(data['chat']['0']['part'].split(','))
            title = data['chat']['0']['name']
            with client:
                client.loop.run_until_complete(create_chat(username, title))
        else:
            print('Waiting to the next command')
        # keyy=input('keyy =\n')
    return 'OK'
