from hockey_data import get_past_scores, get_today_scores
from sql_cnxn import create_game_row

if '__name__' == '__main__':

	try:
		cnxn = mysql.connector.connect(user = '',
								   	   password = '',
								       host = '',
								       database = '')
	except:
		print("Error: Unable to connect to MySQL Server.")

	cursor = cnxn.cursor()

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

	# get_today_scores()

	cnx.commit()

	cursor.close()
	cnx.close()