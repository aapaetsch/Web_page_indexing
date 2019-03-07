import urllib.request as requesting
from html.parser import HTMLParser 
#Holds classes for parsing html and getting links+data in a link

class myParser(HTMLParser):
	#myParser extends HTMLParser
	#mainly for parsing internal links from html and parsing the data related to each link
	def __init__(self):
		HTMLParser.__init__(self)
		#data from a given link
		self.__data = ''
		#links found within that page
		self.__links = []
		#indicator for the most recent tag found
		self.__currentTag = ''
		#attributes of the most recent tag found
		self.__currentAttrs = []

	def handle_starttag(self, tag, attrs):
		# this method is for stripping links, content
		# and recording the most recent tag
		if tag == 'a':
			#if the tag is a link
			for attr in attrs:
				if attr[0] == 'href':
					x = attr[1]
					# if the link is an internal link add it to links
					if x[0] == '/' and len(x)!=1 :
						self.__links.append(x) 
		#go through attributes and check for content 				
		for i in attrs:
			if i[0] == 'content':
				#since the content holds lots of indexable data, we want to grab it.
				#we only grab it if it is not a link. = is excluded as it usually denotes code 
				if 'http' not in i[1] and 'www' not in i[1] and '=' not in i[1]:
					self.__data+=' '
					self.__data+=i[1]
		#update the current tag and its attributes
		self.__currentTag = tag
		self.__currentAttrs = attrs

	def handle_data(self, data):
		#we dont want data from the below tags
		restricted = ['script', 'style', 'link', 'noscript', 'img','',' ' ]
		if self.__currentTag not in restricted:
			#get rid of new lines and such
			data = data.replace('\\n','').replace('\\r','').replace('\\t','')
			if len(data)!=0:
				#add the data to the string of the current link
				self.__data += ' '
				self.__data += data

	#getter methods
	def getData(self):
		#getting the links data
		return self.__data

	def getLinks(self):
		#getting the links in the page
		return self.__links


class grabLinks:
	#for getting all the data related to each internal link, returns a dict
	#dictionary in form of {'mainurl':url, url:data}, if data == None, 
	#link has no data that can be parsed or the url is bad
	def __init__(self, webpage, internal):
		#webpage must be entered as https:// or http:// 
		#followed by address, last char not /
		self.__links = []
		self.__mainUrl = webpage
		self.__visited = {'__mainUrl__':webpage}
		self.__getInternal = internal
	
	def getParsed(self):
		#initialized for the first page
		homePage, homeLinks = self.__getPage(self.__mainUrl)
		if homePage == None:
			return None
		self.__visited[self.__mainUrl] = homePage
		#stop here if we do not want to get all internal links of a webpage
		if self.__getInternal == False:
			return self.__visited

		for i in homeLinks:
			self.__links.append(self.__mainUrl+i)
		while True:
			#stop once we run out of internal links
			if len(self.__links) == 0:
				break
			else: 
				#pop the link off the list
				link = self.__links.pop()
				#if we have not yet visited that link
				if link not in self.__visited and link != None:
					#get the links on that page and the data on that page
					linkData, linkLinks = self.__getPage(link)
					if linkLinks != None:
						for i in linkLinks:
							#i is /link right now, formatted to url/link
							newLink = self.__mainUrl+i
							#check and only add each link if we have not already visited it
							if newLink not in self.__visited:
								self.__links.append(newLink)
					#add the data to the dictionary		
					self.__visited[link] = linkData
		#return links:data dictionary
		return self.__visited			
		

	def __getPage(self, url):
		#private parser method for a page
		#grabs the raw html from a given url
		html = str(self.__grabHTML(url))
		if html == 'None':
			return None, None
		#initiate my parser class
		parser = myParser()
		#give the parser my data
		parser.feed(html)
		#get the data from the parser
		parsedPage = parser.getData()
		#get the links from the parser
		pageLinks = parser.getLinks()

		return parsedPage, pageLinks

	def __grabHTML(self, link):
		#private method for getting the raw html
		try:
			response = requesting.urlopen(link)
			html = response.read()
			response.close()
			
			return html
		except:
			return None

	def getLinks(self):
		return self.__links

	def showparsed(self):#simply for showing what links are in a page
		return self.__findLinks()

def main():
	grab = grabLinks('https://www.the-ambient.com/guides/amazon-alexa-missing-manual-130')
	# grab = grabLinks('something')
	data = grab.getParsed()
	print(data)




# main()
