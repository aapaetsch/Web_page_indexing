from nltk.tokenize import RegexpTokenizer
import nltk
import string

def getTokens(data):#function for getting the tokens for some website
	#only uncomment if you do not have nltk
	#nltk.download('punkt')
	myTokenizer = RegexpTokenizer(r"\w+|\$[\d\.]+|\s+^.")
	#tokenizer
	mainUrl = data['__mainUrl__']
	tokenData = {'__mainUrl__': mainUrl}
    #adding in stemming
	pStemmer = nltk.stem.porter.PorterStemmer()
	#TODO: language recognition so stemming can be accurate
	sStemmer = nltk.stem.snowball.SnowballStemmer('english')


	for key in data:
		# print(key)
		pageTokens = {}
		if key != '__mainUrl__' and data[key] != None:
			tokenizedPage = myTokenizer.tokenize(data[key].lower())
			for i, token in enumerate(tokenizedPage):
				if len(token) == 1:
					token = token.translate(str.maketrans('','',string.punctuation))
				token = token.translate(str.maketrans("\/.", "&&,"))
				if token in pageTokens:
					pageTokens[token]['tf'] += 1
					pageTokens[token]['pos'].append(i)
				else:
					if len(token) > 0 and "'" not in token:
						if i + 1 < len(tokenizedPage):
							if "'" in tokenizedPage[i + 1]:
								if "'s" not in tokenizedPage[i + 1]:
									token += tokenizedPage[i + 1]
						pageTokens[token] = {'tf':1, 'pos':[i]}
			# print(pageTokens)
			tokenData[key] = pageTokens
	return tokenData
