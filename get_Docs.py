class getDocs:
	def __init__(self, query, path):
		self.__query = query
		self.__path = path
		self.__corpus = None

	def grab_relavent(self):
		
		self.__getCorpus()
		docDict = {}
		completedRetrieval = {}
		phrases = {}

		for i in self.__query:
			if " " not in i:
				x = self.__getDocs(i)
				if x != None:
					docDict[i] = x
			else:
				similarDocs = self.__handelPhrase(i)
				if similarDocs != None:
					phrases[i] = similarDocs
		docTokens = {}
		temp = []
		
		for i in docDict:
			temp += docDict[i]

		for key in phrases:
			temp += phrases[key]

		allDocs = np.unique(temp)
		wd = {}
		for i in allDocs:
			with open(self.__path+i+'.json' , 'r') as f:
				document = json.load(f)
			retrieved = {}
			add = False
			for token in self.__query:
				if " " not in token:
					if token in document:
						retrieved[token] = {'tf':document[token]['tf']}
#................................................

	def __calcPhrase(self, document, token):
		
		tokens = token.split(' ')
		hits = 0
		first = document[token[0]]
		subtokens = len(tokens)
		Max = len(first['pos'])

		for i in range(Max):
			sequental = True
			position = first['pos'][i]
			for j in range(1, subtokens):
				if position + 1 in document[tokens[j]]['pos']:
					position += 1
				else:
					sequental = False
					break
			if sequental:
				hits += 1
		if hits != 0:
			tf = 1 + log10(hits)
			return {'tf':tf}, {'count':hits}
		else:
			return {'tf':0}, {'count':0}


	def __handelPhrase(self, phrase):
		listPhrase = phrase.split(' ')
		allDocs = []
		for i in listPhrase:
			allDocs.append(self.__getDocs(i))
		if None in allDocs:
			return None
		#since sites do not have ids we cannot sort 
		similarDocs = []
		if len(allDocs) == len(listPhrase):
			for i in allDocs[0]:
				match = True
				for j in range(len(allDocs)):
					if (( j != 0 ) and i not in allDocs[j]):
						match = False
						break
				if match == True:
					similarDocs.append(i)
			if len(similarDocs) != 0:
				return similarDocs
			else:
				return None
		else:
			return None
	
	def __getDocs(self, token):
		if token in self.__corpus:
			return self.__corpus[token]['siteIDs']
		else:
			return None

	def __getCorpus(self):
		corpus = self.__path + '__corpus__.json'
		with open(corpus,'r') as f:
			self.__corpus = json.load(f)