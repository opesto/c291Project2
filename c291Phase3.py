from bsddb3 import db

VALID_OPS = ('text', 'name', 'location', 'date', None)

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

def main():
	q = get_query()
	#print(q)

main()
