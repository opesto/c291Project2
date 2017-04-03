from bsddb3 import db
import xml.etree.ElementTree as xmltree
import re
import time
import datetime

VALID_OPS = ('text', 'name', 'location', 'date', None)
MAX_RESULTS = 5

# read query from stdin
def get_query(query):
	query = query.lower()
	for i in range(len(query)):
		if query[i] == ':':
			op = query[:i]
			arg = query[i+1:]
			if op not in VALID_OPS:
				print('invalid operation')
				op = None
			elif op == 'date':
				datePrefix = ':'
				return ((op, arg, datePrefix))
			return((op, arg))
		elif query[i] == '>':
			op = query[:i]
			arg = query[i+1:]
			if op not in VALID_OPS:
				print('invalid operation')
				op = None
			elif op == 'date':
				datePrefix = '>'
				return ((op, arg, datePrefix))
			return((op, arg))
		elif query[i] == '<':
			op = query[:i]
			arg = query[i+1:]
			if op not in VALID_OPS:
				print('invalid operation')
				op = None
			elif op == 'date':
				datePrefix = '<'
				return ((op, arg, datePrefix))
			return((op, arg))
		elif i == len(query) - 1:
			return((None, query))

# print results (tweets)
def print_results_tw(results):
	for result in results:
		for element in result:
			print(element.text)

# search a text field for a keyword
def search_k(keyword, cur, prefix='^[tbln]-'):
	results = []
	_keyword = []
	for i in range(len(keyword)):
		if keyword[i] == '%':
			_keyword.append('.*')
		else:
			_keyword.append(keyword[i])
	if '%' not in keyword:
		_keyword.insert(0, prefix)
	keyword = ''.join(_keyword)
	iterator = cur.current()
	while iterator:
		if re.search(keyword, iterator[0].decode('utf-8'), flags=re.I | re.M):
			results.append(iterator[1])
		iterator = cur.next()
	return (results, None)

# print tweets from ids (tids must be iterable)
def fetch_tweets(tids):
	tweet_db = db.DB()
	tweet_db.open('tw.idx')
	tweet_cur  = tweet_db.cursor()
	raw_tweets = []
	for tid in tids:
		raw_tweets.append(tweet_cur.set(tid))
	tweets = []
	for tweet in raw_tweets:
		parsed_tweet = xmltree.fromstring(tweet[1])
		print(parsed_tweet[4][0].text)
		print(parsed_tweet[2].text)
		print('{}\n'.format(parsed_tweet[1].text))

def search_all_terms(database, query, ids, resume):
	cur = database.cursor()
	cur.first()
	status = search_k(query[1], cur)
	results = status[0]
	results = set(results)
	ids.append(results)
	cur.close()

def search_field(database, query, ids):
	# I moved to regex for the wildcard functionality and in doing so
	# made this a bit easier for you, when you call the search_k function
	# it now has an optional argument called prefix that affects what matches
	# long story short, it looks like
	# ^[tbln]-
	# and will match for any characters in the square brackets
	# i.e.:
	# ^[t]-			makes it match any term of the form t-
	# ^[tn]-		matches terms like t- or n-
	# etc
	return

def search_dates(database, query, ids):
	cur = database.cursor()
	cur.first()
	results = []
	argDate = query[1]
	argDate = time.strptime(argDate, "%Y/%m/%d")
	
	#Alternative format, if we wish to compare numbers instead of strings
	#argDate = time.mktime(datetime.datetime.strptime(argDate, "%Y/%m/%d").timetuple())	
	
	#case1: provided date is an exact match (datePrefix = ':')
	if query[2] == ':':
		iterator = cur.current()
		while iterator:
			if query[1] == iterator[0].decode('utf-8'):
				results.append(iterator[1])
			iterator = cur.next()

	#case2: provided date is greater than argument (datePrefix = '>')
	elif query[2] == '>':
		iterator = cur.current()
		while iterator:
			curDate = iterator[0].decode('utf-8')
			curDate = time.strptime(curDate, "%Y/%m/%d")
			if curDate <= argDate:
				iterator = cur.next()
			else:
				results.append(iterator[1])
				iterator = cur.next()

	#case3: provided date is less than argument (datePrefix = '<')
	elif query[2] == '<':
		iterator = cur.current()
		while iterator:
			curDate = iterator[0].decode('utf-8')
			curDate = time.strptime(curDate, "%Y/%m/%d")
			if curDate >= argDate:
				iterator = cur.next()
			else:
				results.append(iterator[1])
				iterator = cur.next()

	ids.append(results)
	cur.close()


def main():
	queryList = input('query? ').split(' ')
	queries = []
	for i in range(len(queryList)):
		queryList[i] = get_query(queryList[i])
	print()
	ids = []
	for query in queryList:
		database = db.DB()
		if query[0] == None:
			database.open('te.idx')
			resume = None
			search_all_terms(database, query, ids, resume)
			database.close()
		elif query[0] == 'date':
			#kiefer
			database.open('da.idx')
			search_dates(database, query, ids)
			database.close()
		elif query[0] in ('location', 'name', 'text'):
			#olivier
			database.open('te.idx')
			search_field(database, query, ids)
			database.close()
	final_ids = ids[0]
	for i in range(1, len(ids)):
		final_ids = final_ids & ids[i]
	final_ids = list(final_ids)
	fetch_tweets(final_ids)
	
main()
