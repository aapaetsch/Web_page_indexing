import Link_Grabber as linkGrab
import dbFormatting as db
import get_Tokens as tkn
import sys, os
class indexCreator:
	def __init__(self):
		self.__isWindows = self.__systemCheck()

	def indexCreation(self):
	
		links = self.__requestLinks()
		if links == None:
			print('No valid links entered.')
			sys.exit(0)
		for link in links:
			item = linkGrab.grabLinks(link)
			data = item.getParsed()
			print(data)
			if data != None:
				tokenizedData = tkn.getTokens(data)
				print(tokenizedData)
			else:
				print('Bad Link:',link)

	def __requestLinks(self):
		self.__systemCheck()
		self.clear()
		print("Links are entered one at a time when prompted to do so.")
		print("It is best if you start links with http:// or https://.")
		print("Type 'done' or 'd' after you enter your final link to be indexed.")
		links = []
		while True:
			link = str(input('Please enter a valid URL> ')).lower()
			if link == 'done' or link == 'd':
				if len(links) == 0:
					return None
				else:
					return links
			else:
				if link[:8] == 'https://':
					links.append(link)
				elif link[:7] == 'http://':
					links.append(link)
				else:
					links.append('https://'+link)

	def clear(self):
		#for clearing input
		if self.__isWindows == True:
			os.system('cls')
		else:
			os.system('clear')

	def __systemCheck(self):
		#checks the type of system you are on
		if sys.platform == 'win32':
			self.__isWindows = True
		else:
			self.__isWindows = False

if __name__ == '__main__':
	ic = indexCreator()
	ic.indexCreation()