import base64, requests, time, json
from sql_cnxn import create_game_row


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
					game_data = (game['game']['awayTeam']['Abbreviation'],
								 game['awayScore'],
								 game['game']['homeTeam']['Abbreviation'],
								 game['homeScore'])
					create_game_row(game_data)
			
			except KeyError:
				pass

			date = date + 1

	except ValueError:
		pass


# TODO: Return JSON data of today's games
# Will not work until season start
def get_today_scores():

	try:

		response = requests.get(
			url = "https://api.mysportsfeeds.com/v1.1/pull/nhl/latest/scoreboard.json",
			params = {
				"fordate": time.strftime("%Y%m%d"),
			},
			headers = {
			"Authorization": "Basic " + base64.b64encode('{}:{}'.format('bewal416','').encode('utf-8')).decode('ascii')
			}
		)

		today_games_json = json.loads(response.content.decode('utf-8'))

		try:
		
			for game in today_games_json['scoreboard']['gameScore']:

				game_data = (game['game']['awayTeam']['Abbreviation'],
							 game['awayScore'],
							 game['game']['homeTeam']['Abbreviation'],
							 game['homeScore'])
				create_game_row(game_data)

		except KeyError:
			pass

	except ValueError:
		pass





