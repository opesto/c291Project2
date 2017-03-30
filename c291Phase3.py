from bsddb3 import db
import xml.etree.ElementTree as xmltree

VALID_OPS = ('text', 'name', 'location', 'date', None)
MAX_RESULTS = 5

# read query from stdin
def get_query(query):
	for i in range(len(query)):
		if query[i] == ':':
			op = query[:i]
			arg = query[i+1:]
			if op not in VALID_OPS:
				print('invalid operation')
				op = None
			return((op, arg))
		elif i == len(query) - 1:
			return((None, query))

# print results (tweets)
def print_results_tw(results):
	for result in results:
		for element in result:
			print(element.text)

# search a text field for a keyword
def search_k(keyword, cur, num=float('inf'), resume=None):
	if resume:
		iterator = cur.set(resume)
	else:
		iterator = cur.first()
	results = []
	while iterator:
		if keyword in iterator[0].decode('utf-8'):
			results.append(iterator[1])
		if len(results) >= num:
			return (results, iterator[0])
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

def search_all_terms(database, query, ids):
	cur = database.cursor()
	done = False
	resume = None
	while not done:
		status = search_k(query[1], cur, MAX_RESULTS, resume)
		resume = status[1]
		results = status[0]
		results = set(results)
		ids.append(results)
		if resume is None:
			done = True
		else:
			inp = input('\n See next {} results (y/n)?'.format(MAX_RESULTS))
			if inp == 'n':
				done = True
	cur.close()

def search_field(database, query, ids):
	...

def search_dates(database, query, ids):
	...

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
			search_all_terms(database, query, ids)
			database.close()
		elif query[0] == 'dates':
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
