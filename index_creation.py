import Link_Grabber as linkGrab
import dbFormatting as db
import get_Tokens as tkn
import sys, os
class indexCreator:
	def __init__(self):
		self.__isWindows = self.__systemCheck()
		self.__corpus = {}
		
	def indexCreation(self):
	
		links = self.__requestLinks()
		self.clear()
		if links == None:
			print('No valid links entered.')
			sys.exit(0)
		print('If you are adding to your index, please enter that folder.')
		folder = str(input('What would you like to name the index folder?> ')).lower().strip('.')
		if folder == '':
			print('Invalid Folder Name.')
			sys.exit(0)
		for link in range(len(links)):
			item = linkGrab.grabLinks(links[link][0], links[link][1])
			data = item.getParsed()
			# print(data)
			if data != None:
				tokenizedData = tkn.getTokens(data)
				print('Finished with:', link)
				# print(tokenizedData)

			else:
				print('Bad Link:',link)


	def __requestLinks(self):
		self.__systemCheck()
		self.clear()
		print("Links are entered one at a time when prompted to do so.")
		print("It is best if you start links with http:// or https://.")
		print("Type 'done' or 'd' after you enter your final link to be indexed.\n")
		
		links = []
		while True:
			link = str(input('Please enter a valid URL> ')).lower()
			
			
			if link == 'd' or link == 'done':
				internal = 'n'
			else:
				internal = str(input("Would you like to get all pages for this site?(y/n)> ")).lower()
			
			
			if internal == 'y' or internal == 'yes':
				internl = True
			else:
				internl = False
			if link == 'done' or link == 'd':
				if len(links) == 0:
					return None
				else:
					return links
			else:
				if link[:8] == 'https://':
					links.append((link, internl))
				elif link[:7] == 'http://':
					links.append((link, internl))
				else:
					links.append((('https://'+link),internl))

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