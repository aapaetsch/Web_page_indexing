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
<<<<<<< HEAD

	#TODO: language recognition so stemming can be accurate
	pStemmer = nltk.stem.porter.PorterStemmer()
	sStemmer = nltk.stem.snowball.SnowballStemmer('english')
	stopWords = list(set( nltk.corpus.stopwords.words('english')))
=======
	pStemmer = nltk.stem.porter.PorterStemmer()
	#TODO: language recognition so stemming can be accurate
	sStemmer = nltk.stem.snowball.SnowballStemmer('english')
>>>>>>> 2ae7f28e84a2d039fbf20d0a77dbcd6c55de99fb


	for key in data:
		# print(key)
		pageTokens = {}
		if key != '__mainUrl__' and data[key] != None:
			tokenizedPage = myTokenizer.tokenize(data[key].lower())
			for i, token in enumerate(tokenizedPage):
				if token in stopWords:
					token = ''

				if len(token) == 1:
					token = token.translate(str.maketrans('','',string.punctuation))
				token = token.translate(str.maketrans("\/.", "&&,"))
				token = sStemmer.stem(pStemmer.stem(token))

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
