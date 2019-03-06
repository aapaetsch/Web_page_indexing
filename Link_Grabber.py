import urllib.request as requesting
from html.parser import HTMLParser 
import sys, os

#Grabbs all links on a web page
#format the input link elsewhere
class myParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.__data = []
		self.__links = []

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			print("Start tag:", tag)
			for attr in attrs:
				print("attr:", attr)
		else:
			for i in attrs:
				if i[0] == 'content':
					print(i[1], 'test')
	# def handle_endtag(self, tag):
	# 	print("Encountered an end tag :", tag)
	def handle_data(self, data):
		data = data.replace('\\n','').replace('\\r','')
		if len(data)!=0:
			self.__data.append(data)

	def getData(self):
		return self.__data

class grabLinks:
	def __init__(self, webpage):
		#webpage must be entered as https:// or http:// 
		#followed by address, last char not /
		self.__links = []
		self.__mainUrl = webpage
		self.__visited = []

	
	def getParsed(self):
		html = str(self.__grabHTML(self.__mainUrl))
	
		parser = myParser()
		parser.feed(html)
		print(parser.getData())
	def __grabHTML(self, link):
		
		try:
			
			response = requesting.urlopen(link)
			html = response.read()
			response.close()
			
			return html
		except:
			return None

	def getLinks(self):
		return self.__links

	def showparsed(self):
		return self.__findLinks()

def main():
	grab = grabLinks('http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html')
	data = grab.getParsed()
	print(data)




main()
