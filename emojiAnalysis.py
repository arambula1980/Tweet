import csv

def readCSV ():
	with open('coors.csv', mode='r') as infile:
	    reader = csv.reader(infile)
	    with open('coors_new.csv', mode='w') as outfile:
	        writer = csv.writer(outfile)
	        mydict = {rows[0]:rows[1] for rows in reader}

def main():
	print "hello"

	reader = csv.DictReader(open('EmojiSentiment.csv'))

	print reader

	result = []
	
	result = list(reader)


	# with open('EmojiSentiment.csv', mode='r') as infile:
	#     reader = csv.reader(infile)
	#     with open('coors_new.csv', mode='w') as outfile:
	#         writer = csv.writer(outfile)
	#         mydict = {rows[0]:rows[6] for rows in reader}


main()