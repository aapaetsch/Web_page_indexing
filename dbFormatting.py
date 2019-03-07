import numpy as np
import os
import json
from math import log10

class dbCreate:
	def __init__(self, path):
		self.__path = path

	def __tfCalc(self,count):
		return 1 + log10(count)

	def createJson(self, link, elements, corpus, weights): # add weighting later
		link = link.replace('https://','').replace('http://','').replace('/','__')
		file = self.__path + link + '.json'
		if os.path.isfile(file) == True:
			print('File already exists:', file)
			return corpus, weights
		document = {}
		for key in elements:
			if key != '__mainUrl__':
				for token in elements[key]:
					count = elements[key][token]['tf']
					tokenPositions = elements[key][token]['pos']
					corpus['__total__'] += count
					corpus['__siteTotal__'] += 1
					tokenFrequency = self.__tfCalc(count)
					document[token] = {'tf':tokenFrequency, 'count':count, 'pos':tokenPositions}
					corpus, weights = self.__corpInsert(corpus, token, link, weights, count)
				with open(file, mode='w') as f:
					json.dump(document, f)
				return corpus, weights

	def createCorpus(self,corp, weights):
		for key in corp:
			if key is not "__total__" and key is not "__siteTotal__":
				corp[key] = {'count':weights[key], 'sitIDs':corp[key]}
		file = self.__path+'__corpus__.json'
		with open(file, mode='w') as f:
			json.dump(corp, f)

	def __corpInsert(self,corp, key, siteID, weight, count):
		try:
			weight[key] += int(count)
			corp[key].append(siteID)
		except:
			weight[key] = int(count)
			corp[key] = [siteID]
		return corp, weight

	# def deletesite(self, corp, link, weight):
	# 	link = link.replace('https://','').replace('http://','').replace('/','__')
	# 	file = self.__path+link+'.json'
	# 	with open(file,'r') as f:
	# 		document = json.load(f)
	# 	for token in docu
	# 	for i in corp:
	# 		if i != "__total__":


		# os.remove()

	def folderCheck(self):
		try:
			os.stat(self.__path)
		except:
			os.mkdir(self.__path)