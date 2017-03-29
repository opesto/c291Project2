from bsddb3 import db
import xml.etree.ElementTree as xmltree

VALID_OPS = ('text', 'name', 'location', 'date', None)
MAX_RESULTS = 5

def get_query():
	query = input('query? ')
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

def print_results_tw(results):
	for result in results:
		for element in result:
			print(element.text)

def search_k(keyword, cur, num=float('inf'), resume=None):
	if resume:
		iterator = cur.set(resume)
	else:
		iterator = cur.first()
	results = []
	while iterator:
		tweet = xmltree.fromstring(iterator[1])
		if keyword in tweet[2].text:
			results.append(tweet)
		if len(results) >= num:
			return (results, iterator[0])
		iterator = cur.next()
	return (results, None)

def main():
	q = get_query()
	print()
	database = db.DB()
	if q[0] == 'text':
		database.open('tw.idx')
		cur = database.cursor()
		done = False
		resume = None
		while not done:
			status = search_k(q[1], cur, MAX_RESULTS, resume)
			resume = status[1]
			results = status[0]
			print_results_tw(results)
			if resume is None:
				print('End of results\n')
				done = True
			else:
				inp = input('\n See next {} results (y/n)?'.format(MAX_RESULTS))
				if inp == 'n':
					done = True
		cur.close()
		database.close()
	
main()
