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
mode = 'BO3'
maps = ['Dust2', 'Inferno', 'Overpass']
map_icon = ['www.hosting.com/img/dust2_icon.png', 'www.hosting.com/img/Inferno_icon.png',
            'www.hosting.com/img/overpass_icon.png']
team_names = ['Astralis', 'ViCi']

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
    data['Mode'] = mode

    data['Maps'][0]['map1'][0]['name'] = maps[0]
    data['Maps'][0]['map1'][0]['map_icon'] = map_icon[0]

    data['Maps'][0]['map2'][0]['name'] = maps[1]
    data['Maps'][0]['map2'][0]['map_icon'] = map_icon[1]

    data['Maps'][0]['map3'][0]['name'] = maps[2]
    data['Maps'][0]['map3'][0]['map_icon'] = map_icon[2]

    data['Team1'][0]['name'] = team_names[0]

    #WIP -->  <--

    try:
        while True:
            pusher_client.trigger('my-channel', 'my-event', str(data))
            time.sleep(10)
    except KeyboardInterrupt:
        print('Dongle STOPPED!')


main()
