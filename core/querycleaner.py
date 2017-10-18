def querycleaner(query):
	query = str(query)
	querylen = len(query)
	query = query[2:querylen-1]
	query = query.replace('\\n','\n')
	print(query)
	query = query.replace('\n',' ')
	query = query.replace('. ',' ')
	query = query.replace(': ',' ')
	return query