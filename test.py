import urllib.request as requesting
from html.parser import HTMLParser 
import sys, os


class myParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.__data = {}
		self.__lastTag = ''
		self.__lastAttr = ''
		self.__links = []
	def handle_starttag(self, tag, attrs):
		self.__lastTag = tag
		self.__lastAttr = attrs
		
		print('tag:', tag,'\n\tattrs:', attrs)

	def handle_data(self, data):

		print('\tdata:',data)
		

class getHTML:
	def __init__(self, URL):
		self.__htmlData = {}
		self.__mainUrl = URL
	def __getpage(self, url):
		html = str(self.__grabHTML(self.__mainUrl))
		parser = myParser()
		parser.feed(html)


	def __grabHTML(self, link):
		
		try:
			
			response = requesting.urlopen(link)
			html = response.read()
			response.close()
			
			return html
		except:
			return None
	def activate(self):
		self.__getpage(self.__mainUrl)


grab = getHTML('https://kite.com/python/docs/HTMLParser.HTMLParser')
grab.activate()