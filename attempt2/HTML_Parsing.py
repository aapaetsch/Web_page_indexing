import urllib.request as requesting
from html.parser import HTMLParser

class myParser(HTMLParser):
    #my parser extends html parser
    #for parsing internal links, but will be reused for parsing data

    def __init__(self):
        HTMLParser.__init__(self)
        self.__data = ''
        self.__internalLinks = []
        self.__externalLinks = []

        self.__currentTag = ''
        self.__currentAttrs = []
        self.__recordExternal=False

    def handle_starttag(self, tag, attributes):
        if tag == 'a':
            print("found link:", tag, attributes)
            for attribute in attributes:
                if attribute[0] == 'href':
                    content = attribute[1]
                    self.__addLink(content)         

        self.__currentTag = tag
        self.__currentAttrs = []
    

    #<---These methods add links--->
    def __addLink(self, link):
        print("attempting to add:",link)
        if link[0] == '/' and len(link) != 1:
            self.__addInternalLink(link)
        elif len(link) != 0 and len(link)!= 1:
            self.__addExternalLink(link)

    def __addInternalLink(self, link):
        self.__internalLinks.append(link)

    def __addExternalLink(self, link):
        if self.__recordExternal:
            self.__externalLinks.append(link)

    #<---These methods are getters --->
    def getData(self):
        return self.__data

    def getInternalLinks(self):
        return self.__internalLinks

    def getExternalLinks(self):
        return self.__externalLinks
    
    #<---These methods clear data from the class--->
    def clearExternalLinks(self):
        self.__externalLinks = []

    def clearInternalLinks(self):
        self.__internalLinks = []

    def clearAllLinks(self):
        self.clearinternalLinks()    
        self.clearExternalLinks()

    def clearData(self):
        self.__data = ''

def grablinks(url):
    #this grabs the links from the raw html 
    parser = myParser()    
    data = getHTML(url)
    if data != None:
        data = str(data)
        parser.feed(data)
        print(parser.getInternalLinks())
        print(parser.getExternalLinks())
        

def getHTML(url):
    try:
        response = requesting.urlopen(url)
        RAW_HTML = response.read()
        response.close()
        return RAW_HTML
    except:
        return None
grablinks("https://en.wikipedia.org/wiki/Main_page")
