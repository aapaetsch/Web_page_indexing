import urllib.request as requesting
from HTML_Parsing import myParser as parser

class linkParser(HTMLParser):
    def __init__(self):
        
        HTMLParser.__init__(self)

        self.__internalLinks = []
        self.__externalLinks = []
        self.__recordInternalLinks = 1
        self.__recordExternalLinks = 0

    def handle_starttag( self, tag, attributes):
        if tag == 'a':
            for a in attributes:
                if a[0] = 'href':
                    content = a[1]
                    self.__addLink(content)

    #<---METHODS TO ADD LINKS--->
    def __addLink(self,link):
        if link[0] == '/' and len(link) != 1 and self.__recordInternalLinks:
            self.__internalLinks.append(link)

        elif len(link) != 0 and len(link) != 1 and self.__recordExternalLinks:
            self.__externalLinks.append(link)

    #<---GETTERS--->
    def getInternalLinks(self):
        return self.__internalLinks
    def getExternalLinks(self):
        return self.__externalLinks
    #<---Clear Links--->

    def clearExternalLinks(self):
        self.__externalLinks = []

    def clearInternalLinks(self):
        self.__internalLinks = []

def findLinks(URL):
    parser = linkParser()
    data = getHTML(URL)
    if data != None:
        parser.feed(str(data))
        print(parser.getInternalLinks())

def getHTML(url):
    try:
        RAW_HTML = requesting.urlopen(url).read()
        response.close()
        return RAW_HTML
    except:
        return None
findLinks('https://en.wikipedia.org')
