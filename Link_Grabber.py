import urllib.request
import sys, os

#Grabbs all links on a web page
def grabHTML(link):
	if link[:3] == 'www':
		link = 'https://'+link
	elif link[:7] != 'https://' or link[:6] != 'http://':
		link = 'https://'+link
	data = urllib.request.Request(link)
	print(data)
grabHTML('www.orangeavocado.ca')
