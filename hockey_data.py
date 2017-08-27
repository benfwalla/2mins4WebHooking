import base64
import requests
import time
import json


# TODO: Return tuple data of the NHL 2015-2016 and 2016-2017 seasons
def get_past_scores(beg_year, end_year, beg_date, end_date):

	date = beg_date

	try:

		while date <= end_date:

			response = requests.get(
				url = "https://api.mysportsfeeds.com/v1.1/pull/nhl/{}-{}-regular/scoreboard.json".format(beg_year, end_year),
				params = {
					"fordate" : "{}".format(date)
				},
				headers = {
				"Authorization": "Basic " + base64.b64encode('{}:{}'.format('bewal416','').encode('utf-8')).decode('ascii')
				}
			)
			
			all_games_json = json.loads(response.content.decode('utf-8'))

			try:
				for game in all_games_json['scoreboard']['gameScore']:
					game_data = (game['game']['date'],
								 game['game']['awayTeam']['Abbreviation'],
								 game['awayScore'],
								 game['game']['homeTeam']['Abbreviation'],
								 game['homeScore'])
					# Placeholder. This is where SQL INSERT goes.
					print(game_data)
			except KeyError:
				pass

			date = date + 1

	except ValueError:
		pass

# get_past_scores(2015, 2016, 20151007, 20151031)
# get_past_scores(2015, 2016, 20151101, 20151130)
# get_past_scores(2015, 2016, 20151201, 20151231)
# get_past_scores(2015, 2016, 20160101, 20160127)
# get_past_scores(2015, 2016, 20160201, 20160229)
# get_past_scores(2015, 2016, 20160301, 20160331)
# get_past_scores(2015, 2016, 20160401, 20160410)

# get_past_scores(2016, 2017, 20161012, 20161030)
# get_past_scores(2016, 2017, 20161101, 20161130)
# get_past_scores(2016, 2017, 20161201, 20161231)
# get_past_scores(2016, 2017, 20170101, 20170131)
# get_past_scores(2016, 2017, 20170201, 20170228)
# get_past_scores(2016, 2017, 20170301, 20170331)
# get_past_scores(2016, 2017, 20170401, 20170409)


# TODO: Return JSON data of today's games
# Will not work until season start
def get_today_scores():

	response = requests.get(
		url = "https://api.mysportsfeeds.com/v1.1/pull/nhl/current/scoreboard.json",
		params = {
			"fordate": str(int(time.strftime("%Y%m%d"))),
		},
		headers = {
		"Authorization": "Basic " + base64.b64encode('{}:{}'.format('bewal416','').encode('utf-8')).decode('ascii')
		}
	)

	parsed_json = json.loads(response.content.decode('utf-8'))

	# Placeholder. This is where MySql cnxn goes
	return parsed_json






