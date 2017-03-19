import sys
import requests
import tweepy
import oauth2
import json

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
	ConsumerKey = "pVWEU6OPLfznZ1cTrCCOdFFQl"
	ConsumerSecret = "ljofJTXL3NBZNPBI0fc8qXC5cLMOPRFhwP5iR0EprKBCV9qF23"
	auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
	api = tweepy.API(auth)
	new_tweets = api.user_timeline("GSElevator", count=50)

	result = oauth_req("https://api.twitter.com/1.1/search/tweets.json?q=%23michigan&result_type=mixed&count=4", 'abd','hey')
	res = json.loads(result)
	print res["statuses"][0]["text"]
	# result = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=%40AAPL")
	# print result.text

def main():
	ticker = sys.argv[1]
	print get_symbol(ticker)
	collectTweets("hey")

main()

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

