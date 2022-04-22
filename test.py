import requests
import json
import time
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
SESSION_STRING = os.environ.get('SESSION_STRING')

TIME_SLEEP=10

URL="http://127.0.0.1:8000/tg/"
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



async def send_msg(username):
    # Now you can use all client methods listed below, like for example...
    await client.send_message(username, 'I will create a chat instead of this msg')


def main():

    print('start')
    for i in range(5):

        time.sleep(TIME_SLEEP)

        data=get_data(URL)
        print(data['flag'])
        if data['flag']:
            with client:
                client.loop.run_until_complete(send_msg(Polina))
        else:
            print('Waiting to the next command')


if __name__ == "__main__":
    main()