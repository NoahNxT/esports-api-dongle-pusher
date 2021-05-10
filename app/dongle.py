import pusher
import random
import time
import json
from datetime import datetime

game = 'lol:GO'
icon = 'www.hosting.com/img/csgo_icon.png'
banner = "www.hosting.com/img/iemsummerbanner.png"
tournament = 'IEM Summer 2021'
date = datetime.today().strftime('%d-%m-%Y ')
now = datetime.now()
timenow = now.strftime('%I:%M %p')


pusher_client = pusher.Pusher(
    app_id='1201428',
    key='1b52ec7212fce7142eee',
    secret='fb16863082f2518c752e',
    cluster='eu',
    ssl=True
)

print("E-sports Fake Data Dongle - STARTED")
print("Press Ctrl-C to exit")


def main():
    with open('./data.json') as f:
        data = json.load(f)
    data['Game'] = game
    data['Icon'] = icon
    data['Banner'] = banner
    data['Tournament'] = tournament
    data['Date'] = date
    data['Time'] = str(timenow)

    try:
        while True:
            pusher_client.trigger('my-channel', 'my-event', str(data))
            time.sleep(10)
    except KeyboardInterrupt:
        print('Dongle STOPPED!')


main()
