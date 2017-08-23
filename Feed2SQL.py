import base64
import requests
import time
import json


# Returns the JSON data of yesterday's MLB scores
def get_yesterdays_mlb_scores():

    response = requests.get(
        url='https://api.mysportsfeeds.com/v1.1/pull/mlb/current/scoreboard.json',
        params={
            "fordate": str(int(time.strftime("%Y%m%d"))-1)
        },
        headers={
            "Authorization": "Basic " + base64.b64encode('{}:{}'.format('bewal416','').encode('utf-8')).decode('ascii')
        }
    )

    # .decode('utf-8') will turn JSON from bytes to strings. 
    # json.loads() parses JSON into a recognizable Python object
    parsed_json = json.loads(response.content.decode('utf-8'))

    return parsed_json


# Prints the scores of every game in the MLB yesterday
def list_scores():
	for game in get_yesterdays_mlb_scores()['scoreboard']['gameScore']:
		#print("ID: " + game['game']['ID'])
		print(game['game']['awayTeam']['Abbreviation'] + ": " + game['awayScore'])
		print(game['game']['homeTeam']['Abbreviation'] + ": " + game['homeScore'])
		print()

print(list_scores())

