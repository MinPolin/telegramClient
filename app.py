import requests
import json
import time
import os
from telethon import events


from telethon.tl.custom import Button
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import functions,types
import flask
from flask import request
import asyncio
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
# URL="http://127.0.0.1:5000/tg/"
Polina='MinPolin'
Vlad='whatislove_sakharov'
# 588513947







def get_data(url):
    response = requests.get(url)
    content = response.content.decode()
    data = json.loads(content)

    return data
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def get_client():

    api_hash = API_HASH
    api_id = API_ID
    name = 'admin'
    client=TelegramClient(StringSession(SESSION_STRING), api_id, api_hash,loop=loop)
    client.start()
    return client

@events.register(events.NewMessage(pattern='(?i)hello.+'))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    await event.reply('Hey!')
client = get_client()
client.add_event_handler(handler)


async def create_chat(username,title):

    result = await client(functions.messages.CreateChatRequest(username, title=title))
    print(result.__dict__["chats"][0].__dict__["id"])


async def get_all_dialogs():
    async for dialog in client.iter_dialogs():
        print('{:>14}: {}'.format(dialog.id, dialog.title))
        print(type(dialog.id))
        if dialog.id<0:
            result = await client(functions.messages.DeleteChatRequest(chat_id=abs(dialog.id)))
            print(result)

async def send_msg(username,msg):
    # Now you can use all client methods listed below, like for example...

    await client.send_message(username, msg, parse_mode="html")

@app.route("/", methods=['GET', 'POST'])
def main():
    print('smth3')
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json['name'], json['parts'])
        username = list(json['parts'].split(','))
        # username = (Polina,)
        print(username)
        title=json['name']
        loop.run_until_complete(create_chat(username,title))


    else:
        print(content_type)


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


@app.route('/new_user/', methods=['GET', 'POST'])
def new_user():
    print('smth_new')
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json['msg'], json['chat'])
        chat = int(json['chat'])
        msg = str(json['msg'])
        loop.run_until_complete(send_msg(chat,msg))


    else:
        print(content_type)

    return {'data': 'v'}
@app.route('/simple_send/', methods=['GET', 'POST'])
def simple_send():
    print('smth_simple')
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json['msg'], json['user'])

        user = json['user']
        # user = Polina
        msg = str(json['msg'])
        loop.run_until_complete(send_msg(user, msg))

    else:
        print(content_type)

    return {'data': 'v'}
