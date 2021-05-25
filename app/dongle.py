#!/usr/bin/python

import pusher
import random
import time
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

status = ['Upcoming', 'Live', 'Ended']
map_playing = ['none', os.environ.get('MAP1_NAME'), os.environ.get('MAP2_NAME'), os.environ.get('MAP3_NAME')]
date = datetime.today().strftime('%d-%m-%Y ')
now = datetime.now()
timenow = now.strftime('%I:%M %p')
mode = 'BO1'
game_maps = [os.environ.get('MAP1_NAME'), os.environ.get('MAP2_NAME'), os.environ.get('MAP3_NAME')]
map_icon = [os.environ.get('MAP1_ICON'),
            os.environ.get('MAP2_ICON'),
            os.environ.get('MAP3_ICON')]
team_names = [os.environ.get('TEAM1_NAME'), os.environ.get('TEAM2_NAME')]
team_logos = [os.environ.get('TEAM1_LOGO'),
              os.environ.get('TEAM2_LOGO')]
team_factors = [1.86, 1.14]

team1_player_names = ['NuKe', 'PlaZz', 'Pasha Biceps', 'Fallen', 'Scream']

team2_player_names = ['Karma', 'DeadShoT', 'SwarmEE', 'snAX', 'Elen']

pusher_client = pusher.Pusher(
    app_id=os.environ.get('APP_ID'),
    key=os.environ.get('KEY'),
    secret=os.environ.get('SECRET'),
    cluster=os.environ.get('CLUSTER'),
    ssl=True
)

print("E-sports Fake Data Dongle - STARTED")
print("Press Ctrl-C to exit")

with open('./data.json') as f:
    data = json.load(f)


    def warmup():

        data['Game'] = os.environ.get('GAME_NAME')
        data['Icon'] = os.environ.get('GAME_ICON')
        data['Banner'] = os.environ.get('TOURNAMENT_BANNER')
        data['Tournament'] = os.environ.get('TOURNAMENT_NAME')
        data['Date'] = date
        data['Time'] = str(timenow)
        data['Mode'] = mode
        data['Status'] = status[0]
        data['Map_playing'] = map_playing[0]
        data['Team1'][0]['Score'] = 0
        data['Team2'][0]['Score'] = 0


        """
            Set all K / A / D / MVP amount of players to 0 
        """
        for j in range(1, 3):
            for i in range(0, 5):
                data['Team' + str(j)][0]['Team'][0]['Player' + str(i + 1)][0]['Kills'] = 0
                data['Team' + str(j)][0]['Team'][0]['Player' + str(i + 1)][0]['Assists'] = 0
                data['Team' + str(j)][0]['Team'][0]['Player' + str(i + 1)][0]['Deaths'] = 0
                data['Team' + str(j)][0]['Team'][0]['Player' + str(i + 1)][0]['MVP'] = 0

        """
            Set all playable maps 
        """
        for k in range(0, 3):
            data['Maps'][0]['Map' + str(k + 1)][0]['Name'] = game_maps[k]
            data['Maps'][0]['Map' + str(k + 1)][0]['Map_icon'] = map_icon[k]

        """
            Set all teams and their players 
        """
        for j in range(0, 2):
            data['Team' + str(j + 1)][0]['Name'] = team_names[j]
            data['Team' + str(j + 1)][0]['Logo'] = team_logos[j]
            data['Team' + str(j + 1)][0]['Factor'] = team_factors[j]

            for i in range(0, 5):
                data['Team1'][0]['Team'][0]['Player' + str(i + 1)][0]['Name'] = team1_player_names[int(i)]
                data['Team2'][0]['Team'][0]['Player' + str(i + 1)][0]['Name'] = team2_player_names[int(i)]

        """
           If warmup has set all values first run, push to pusher 
           else wai
        """
        if warmup.counter == 1:
            data['Match_id'] = random.randint(1, 9999)
            pusher_client.trigger('csgo', 'match-data-csgo', json.dumps(data))
            warmup.counter += 1

        time.sleep(int(os.environ.get('MESSAGE_INTERVAL')))


    def main():
        warmupcalls = int(os.environ.get('MATCH_WARMUP'))
        warmup.counter = 1

        try:
            """
                Warmup simulation
            """
            for x in range(0, warmupcalls + 1):
                warmup()
                print('Match will start in ' + str(warmupcalls - x) + ' seconds')

            """
                If the status of the game is upcoming change it to Live 
                If the Map that is going to be played isn't set, set it to the first map
            """
            if data['Status'] == status[0] or data['Map_playing'] == map_playing[0]:
                data['Status'] = status[1]
                data['Map_playing'] = map_playing[1]
                pusher_client.trigger('csgo', 'match-data-csgo', json.dumps(data))
                print('The match of ' + os.environ.get('TEAM1_NAME') + ' vs ' + os.environ.get(
                    'TEAM2_NAME') + ' has been started!')

            """
                Start match until a team reached 16 points
            """
            while data['Team1'][0]['Score'] <= 16 or data['Team2'][0]['Score'] <= 16:

                """
                    If team has reached 16 points, set status to ended and exit program
                """
                if data['Team1'][0]['Score'] == 16 or data['Team2'][0]['Score'] == 16:
                    data['Status'] = status[2]
                    pusher_client.trigger('csgo', 'match-data-csgo', json.dumps(data))
                    break

                """
                    Generating Random K / A / D / MVP amount to assign to players in the upcoming round 
                """
                random_kills = [(random.randint(1, 3)), 0, (random.randint(0, 1)), 0, (random.randint(1, 2))]
                random_assists = [(random.randint(1, 3)), 0, (random.randint(0, 1)), 0, (random.randint(1, 2))]
                random_deaths = [(random.randint(0, 1)), (random.randint(0, 1)), (random.randint(0, 1)),
                                 (random.randint(0, 1)), (random.randint(0, 1))]
                random_team = random.randint(1, 2)
                # random_round_time = random.randint(45, 115)
                random_round_time = random.randint(0, 1)

                """
                    Assign random generated amount of K / A / D / MVP to players
                """
                for j in range(1, 3):
                    for i in range(1, 6):
                        data['Team' + str(j)][0]['Team'][0]['Player' + str(i)][0]['Kills'] += random_kills[
                            (random.randint(0, 4))]
                        data['Team' + str(j)][0]['Team'][0]['Player' + str(i)][0]['Assists'] += random_assists[
                            (random.randint(0, 4))]
                        data['Team' + str(j)][0]['Team'][0]['Player' + str(i)][0]['Deaths'] += random_deaths[
                            (random.randint(0, 4))]
                data['Team' + str(random_team)][0]['Team'][0]['Player' + str((random.randint(1, 5)))][0][
                    'MVP'] += 1

                """
                    Add point to team and set match time delay
                """
                data['Team' + str(random_team)][0]['Score'] += 1
                print('Round will last ' + str(random_round_time) + ' seconds')
                time.sleep(random_round_time)
                print(str(data['Team1'][0]['Score']) + ' : ' + str(data['Team2'][0]['Score']))
                pusher_client.trigger('csgo', 'match-data-csgo', json.dumps(data))

        except KeyboardInterrupt:
            print('Dongle STOPPED!')
            exit()

while True:
    main()
    print('Match has ended, in 10 seconds a new match will start!')
    time.sleep(10)
