from bsddb3 import db
import subprocess

#Uniqely sort a file and return the output
def sortFile(file):
	return subprocess.check_output(["sort", "-u", file])

def main():
	DATABASE_TWEETS = "tweets.db"
	DATABASE_TERMS = "terms.db"
	DATABASE_DATES = "dates.db"
	database_tweets = db.DB()
	database_terms = db.DB()
	database_dates = db.DB()
	database_tweets.open(DATABASE_TWEETS,None, db.DB_HASH, db.DB_CREATE)
	database_terms.open(DATABASE_TERMS,None, db.DB_BTREE, db.DB_CREATE)
	database_dates.open(DATABASE_DATES,None, db.DB_BTREE, db.DB_CREATE)


	sortFile("tweets.txt")
	file_tweets = open("tweets.txt", "r")
	for line in file_tweets:
		key_tweet = line[0:9]
		data_tweet = line[10:-1]
	file_tweets.close()

	sortFile("terms.txt")
	file_terms = open("terms.txt", "r")
	for line in file_terms:
		key_term = ""
		data_term = ""
		key = True
		for char in line:
			if char != ":" and key:
				 key_term = key_term+char
			elif char != ":" and not key:
				data_term = data_term+char
			else:
				key = False
		data_term = data_term[:-1]
	file_terms.close()

	sortFile("dates.txt")
	file_dates = open("dates.txt", "r")
	for line in file_dates:
		key_date = line[0:10]
		data_date = line[11:-1]

	file_dates.close()

	curs_tweets = database_tweets.cursor()
	curs_terms = database_terms.cursor()
	curs_dates = database_dates.cursor()
	curs_tweets.close()
	curs_terms.close()
	curs_dates.close()
	database_tweets.close()
	database_terms.close()
	database_dates.close()


main()
