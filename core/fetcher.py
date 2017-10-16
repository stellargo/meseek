import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	
	#Looks for div tags with class=g and once found, resets: started.
	def handle_starttag(self, tag, attrs):
		if (tag=='div' and attrs==[("class", "g")]):
			self.started=True

	#Invoked when end tag is reached, resets: started, linkbegun, link.
	def handle_endtag(self, tag):
		if (tag=='div' and self.started==True):
			self.started=False
			self.result.append(self.link)
			self.link=''
			self.linkbegun=False

	#Looks for http links and starts adding them to link variable.
	def handle_data(self, data):
		if (self.started==True):
			if (data[0:4]=='http'):
				self.link = self.link + data
				self.linkbegun = True
			elif (self.linkbegun==True):
				self.link = self.link + data

#A function that takes a query to be searched as parameter and gives output in the form of a list 
#which contains all links for that query.
def fetcher(query):
	query = 'https://www.google.co.in/search?q=' + query
	resp = requests.get(query)
	if resp.ok:
		parser = MyHTMLParser()
		parser.started=True
		parser.result = []
		parser.link = ''
		parser.linkbegun = False
		parser.feed(resp.text)
		return parser.result
	else:
		return 1