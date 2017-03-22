import sys
import os
import requests
import tweepy
import oauth2
import json

dow = [
"MMM",
"AXP",
"AAPL",
"BA",
"CAT",
"CVX",
"CSCO",
"KO",
"DD",
"XOM",
"GE",
"GS",
"HD",
"INTC",
"IBM",
"JNJ",
"JPM",
"MCD",
"MRK",
"MSFT",
"NKE",
"PFE",
"PG",
"TRV",
"UNH",
"UTX",
"VZ",
"V",
"WMT",
"DIS"
]

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

#home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', 'abcdefg', 'hijklmnop' )
#print home_timeline
def collectTweets(keyword):
	#ConsumerKey = "pVWEU6OPLfznZ1cTrCCOdFFQl"
	#ConsumerSecret = "ljofJTXL3NBZNPBI0fc8qXC5cLMOPRFhwP5iR0EprKBCV9qF23"
	#auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
	#api = tweepy.API(auth)
	#new_tweets = api.user_timeline("GSElevator", count=50)
	url = "https://api.twitter.com/1.1/search/tweets.json?q=" + keyword + "&result_type=mixed&count=100"
	#returned_tweets = oauth_req("https://api.twitter.com/1.1/search/tweets.json?q=%23michigan&result_type=mixed&count=4", 'abd','hey')
	returned_tweets = oauth_req(url, 'abd','hey')
	res = json.loads(returned_tweets)
	print res["statuses"][0]["text"]
	print len(res["statuses"])
	tweet_text = list()
	for status in res["statuses"]:
		tweet_text.append(status["text"])
	return tweet_text
	# result = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=%40AAPL")
	# print result.text

def sentimentAnalysis(tweets_list):
	#scores_file = open("sentimentstrength/wordwithStrength.txt", "r")
	scores_file = open("SentiWordNet.txt", "r")
	#pos_dict = dict()
	#neg_dict = dict()
	scores_dict = dict()
	tweet_scores = list()

	for line in scores_file:
		line = line.strip()
		if line[0] != "#":
			tmp = line.split()
			word = tmp[4].split("#")
			scores_dict[str(word[0])] = float(tmp[2]) - float(tmp[3])
			#pos_dict[str(word[0])] = float(tmp[2])
			#neg_dict[str(word[0])] = float(tmp[3])
	#print scores_dict

	for each_tweet in tweets_list:
		count = 0.0
		tweet_score = 0.0
		tmp = each_tweet.split()
		for each_word in tmp:
			if each_word.lower() in scores_dict:
				tweet_score = tweet_score + scores_dict[each_word.lower()]
				count = count + 1.0
		print (each_tweet + " " + str(tweet_score))
		if count != 0:
			tweet_scores.append((float(tweet_score)/count))

	total_score = sum(tweet_scores)
	total_score = total_score / len(tweet_scores)
	return total_score


def main():
	ticker = sys.argv[1]
	company_name = get_symbol(ticker)
	tweets = collectTweets(company_name)
	stock_score = sentimentAnalysis(tweets)

main()













