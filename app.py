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

dow = ["MMM","AXP","AAPL","BA","CAT","CVX","CSCO","KO","DD","XOM","GE","GS","HD","INTC","IBM","JNJ","JPM","MCD","MRK","MSFT","NKE","PFE","PG","TRV","UNH","UTX","VZ","V","WMT","DIS"]
# Source: http://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
# Contractions to be used in tokenizer for possessives
contractions = { 
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"I'd": "I would",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I've": "I have",
"isn't": "is not",
"it'd": "it had",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that had",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there had",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we had",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you had",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key="qOaznKRz5VhaSl7Cz6QYH2nB9", secret="LdvYknJa0WZroecT0k1KYdRi7UH8ot0K8HezT5OAC0uLaiTbJk")
    token = oauth2.Token(key="809904932-NnxQCbT29Y97CqdxRMhJMwrxs3DsiLi7Q3hx6nUJ", secret="Zwuw2pCGZopavmKHwbrswVuriCdVAjwY5OeOk97a1uWgT")
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

def create_dict():
	scores_file = open("SentiWordNet.txt", "r")
	scores_dict = dict()
	for line in scores_file:
		line = line.strip()
		if line[0] != "#":
			tmp = line.split()
			word = tmp[4].split("#")
			scores_dict[str(word[0])] = float(tmp[2]) - float(tmp[3])
	return scores_dict

def collectTweets(keyword):
	#ConsumerKey = "pVWEU6OPLfznZ1cTrCCOdFFQl"
	#ConsumerSecret = "ljofJTXL3NBZNPBI0fc8qXC5cLMOPRFhwP5iR0EprKBCV9qF23"
	#auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
	#api = tweepy.API(auth)
	#new_tweets = api.user_timeline("GSElevator", count=50)
	tweet_text = dict()
	url = "https://api.twitter.com/1.1/search/tweets.json?q=" + keyword + "&result_type=recent&count=100"
	returned_tweets = oauth_req(url, 'abd','hey')
	res = json.loads(returned_tweets)
	for status in res["statuses"]:
		tweet_text[status["id"]] = [status["text"], status["user"]["followers_count"]]
		#tweet_text.append(status["text"])
	return tweet_text
	for num in range(0,1):
		#print res["statuses"][0]["text"]
		#print res["statuses"][0]["created_at"]
		#print res["statuses"][0]["user"]["time_zone"]
		url = "https://api.twitter.com/1.1/search/tweets.json" + res["search_metadata"]["next_results"]
		returned_tweets = oauth_req(url, 'abd','hey')
		res = json.loads(returned_tweets)
		for status in res["statuses"]:
			tweet_text.append(status["text"])
	return tweet_text

'''test = ["antithesis contrary it unable",
"Abstinent the battered accessible",
"accessible obliging",
"Battered the wrong"]'''

# Function to tokenize text
def tokenizeText(line, wordNet_dict):
	nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	months = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec.", "January", "February", "March", "April", "June", "July", "August", "September", "October", "November", "December"]
	tokens = []
	words = line.strip().split()

	tmplist = list()
	for word in words:
		word = unidecode(word)
        # APOSTROPHES:
        # Tokenize "'" if in contraction:
		if "'" in word:
			if word in contractions:
				expansion = contractions[word]
				all_words = expansion.split()
				for all_word in all_words:
					tmplist.append(all_word)
		else:
			tmplist.append(word)

	final_tokenized_list = list()
	for tmp_words in tmplist:
		replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
		tmp_words = tmp_words.translate(replace_punctuation)
		tmp_word = tmp_words.split()
		final_tokenized_list.extend(tmp_word)

	return final_tokenized_list

def sentimentAnalysis(tweet_list, scores_dict, tweet_followers):
	count = 0.0
	tweet_score = 0.0
	for each_tweet_word in tweet_list:
		if each_tweet_word.lower() in scores_dict:
			#print "word: ", each_word, "score: ", scores_dict[each_word.lower()]
			tweet_score = tweet_score + scores_dict[each_tweet_word.lower()]
			count = count + 1.0
		#print each_tweet + " " + str(tweet_score/count)
	if count != 0.0:
		weight_factor = math.log(float(tweet_followers), 10)
		return weight_factor*(float(tweet_score)/count)
	else:
		return 0.0

def scoreTweets(all_tweets_scores):
	max_abs_val = math.fabs(all_tweets_scores[0])
	for num in range(1, len(all_tweets_scores)):
		if math.fabs(all_tweets_scores[num]) > max_abs_val:
			max_abs_val = math.fabs(all_tweets_scores[num])

	total_score = 0.0
	for each_tweet_score in all_tweets_scores:
		total_score = total_score + (float(each_tweet_score)/float(max_abs_val))
	total_score_avg = float(total_score)/float(len(all_tweets_scores))
	return total_score_avg

def main():
	ticker = sys.argv[1]
	company_name = get_symbol(ticker)
	scores_dict = create_dict()
	tweets = collectTweets(company_name)
	final_tweet_scores = list()
	for tweet in tweets:
		tokenized_tweets = tokenizeText(tweets[tweet][0], scores_dict)
		final_tweet_scores.append(sentimentAnalysis(tokenized_tweets, scores_dict, tweets[tweet][1]))
	print scoreTweets(final_tweet_scores)

main()




# Notes:
# search for "contrary#1" (only search for first word in line if it has #1 attached)








