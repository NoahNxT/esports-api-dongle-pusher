import pusher
import random
import time
import json
from datetime import datetime

game = 'CS:GO'
icon = 'www.hosting.com/img/csgo_icon.png'
banner = "www.hosting.com/img/iemsummerbanner.png"
tournament = 'IEM Summer 2021'
date = datetime.today().strftime('%d-%m-%Y ')
now = datetime.now()
timenow = now.strftime('%I:%M %p')
mode = 'BO1'
game_maps = ['Dust2', 'Inferno', 'Overpass']
map_icon = ['www.hosting.com/img/dust2_icon.png', 'www.hosting.com/img/Inferno_icon.png',
            'www.hosting.com/img/overpass_icon.png']
team_names = ['Astralis', 'ViCi']
team_logos = ['www.hosting.com/img/astralis.png', 'www.hosting.com/img/vici.png']
team_factors = [1.86, 1.14]
team_scores = [12, 8]

team1_player_names = ['NuKe', 'PlaZz', 'Pasha Biceps', 'Fallen', 'Scream']
team1_player_kills = [27, 19, 12, 9, 3]
team1_player_assists = [6, 3, 9, 8, 14]
team1_player_deaths = [14, 14, 5, 12, 11]
team1_player_mvp = [4, 2, 0, 1, 4]

team2_player_names = ['Karma', 'DeadShoT', 'SwarmEE', 'snAX', 'Elen']
team2_player_kills = [18, 16, 10, 7, 1]
team2_player_assists = [8, 2, 5, 6, 10]
team2_player_deaths = [12, 2, 13, 14, 10]
team2_player_mvp = [0, 1, 0, 1, 2]

delay_message = 1

pusher_client = pusher.Pusher(
    app_id='1201428',
    key='1b52ec7212fce7142eee',
    secret='fb16863082f2518c752e',
    cluster='eu',
    ssl=True
)

print("E-sports Fake Data Dongle - STARTED")
print("Press Ctrl-C to exit")


def maps():
    with open('./data.json') as f:
        data = json.load(f)

    for k in range(0, 2):
        data['Maps'][0]['Map' + str(k + 1)][0]['Name'] = game_maps[k]
        data['Maps'][0]['Map' + str(k + 1)][0]['Map_icon'] = map_icon[k]

        data['Maps'][0]['Map' + str(k + 1)][0]['Name'] = game_maps[k]
        data['Maps'][0]['Map' + str(k + 1)][0]['Map_icon'] = map_icon[k]

        data['Maps'][0]['Map' + str(k + 1)][0]['Name'] = game_maps[k]
        data['Maps'][0]['Map' + str(k + 1)][0]['Map_icon'] = map_icon[k]


def teams():
    with open('./data.json') as f:
        data = json.load(f)

    for j in range(0, 1):
        data['Team' + str(j + 1)][0]['Name'] = team_names[j]
        data['Team' + str(j + 1)][0]['Logo'] = team_logos[j]
        data['Team' + str(j + 1)][0]['Factor'] = team_factors[j]
        data['Team' + str(j + 1)][0]['Score'] = team_scores[j]

        for i in range(0, 4):
            data['Team1'][0]['Team'][0]['Player' + str(i + 1)][0]['Name'] = team1_player_names[int(i)]
            data['Team1'][0]['Team'][0]['Player' + str(i + 1)][0]['Kills'] = team1_player_kills[int(i)]
            data['Team1'][0]['Team'][0]['Player' + str(i + 1)][0]['Assists'] = team1_player_assists[int(i)]
            data['Team1'][0]['Team'][0]['Player' + str(i + 1)][0]['Deaths'] = team1_player_deaths[int(i)]
            data['Team1'][0]['Team'][0]['Player' + str(i + 1)][0]['MVP'] = team1_player_mvp[int(i)]
            data['Team2'][0]['Team'][0]['Player' + str(i + 1)][0]['Name'] = team2_player_names[int(i)]
            data['Team2'][0]['Team'][0]['Player' + str(i + 1)][0]['Kills'] = team2_player_kills[int(i)]
            data['Team2'][0]['Team'][0]['Player' + str(i + 1)][0]['Assists'] = team2_player_assists[int(i)]
            data['Team2'][0]['Team'][0]['Player' + str(i + 1)][0]['Deaths'] = team2_player_deaths[int(i)]
            data['Team2'][0]['Team'][0]['Player' + str(i + 1)][0]['MVP'] = team2_player_mvp[int(i)]


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

    maps()
    teams()

    try:
        while True:
            pusher_client.trigger('my-channel', 'my-event', str(data))
            time.sleep(delay_message)
    except KeyboardInterrupt:
        print('Dongle STOPPED!')


main()
