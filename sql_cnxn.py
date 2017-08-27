import mysql.connector

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

# Creates a new row in a MySQL table
# Input type: tuple of strings (i.e. ('PIT', '4', 'NYR', '2'))
def create_game_row(game_data):

	add_game = ("INSERT INTO gameScore "
                "(away_team, away_score, home_team, home_score) "
                "VALUES (%s, %s, %s, %s)")

	cursor.execute(add_game, game_data)

#create_game_row(('PIT', '4', 'NYR', '2'))