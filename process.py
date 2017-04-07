import sys
import os
import requests
import tweepy
import oauth2
import json
import string
import re
from unidecode import unidecode
import math
import schedule
import time

def main():
	tweets = {}
	path = sys.argv[1]
	words = []
	for f in os.listdir(path):
		infile = open(os.path.join(path, f), 'r')
		while 1:
			line = infile.readline()
			if line == '':
				break
		 	values = line.split(',',1)
		 	id = values[0].split(':')[1]
		 	id = id[:-1]
		 	id = id[1:]
		 	
		 	if id not in tweets:
		 		tweets[id] = values[1]

		infile.close()
	print len(tweets)

main()