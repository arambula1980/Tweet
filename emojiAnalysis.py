import csv

def main():
	print "hello"

	reader = csv.reader(open('EmojiSentiment.csv'))

	print reader

	emojiDict = dict()

	for row in reader:
		emojiDict[row[0]] = row[1]

	print emojiDict


main()