# Twitter Sentiment Analysis for Stock Prediction
EECS 486 Winter 2017 Final Project by Group 8: Benjamin Rathi, Kevin Shah, Yashan Thakkar, Samidha Visai

***

### Description of Project:
We want to collect tweets for a company (given a stock ticker symbol) and perform a sentiment analysis on the tweets to see if one should buy the stock.
 
We do this by first finding the company's information, such as company name and other trademarked names, using a user input of a ticket symbol, and the Yahoo Finance API. From there, we collect tweets using the Twitter Search API. We then tokenize the text and score each tweet based on sentiment. The scores are normalized by length of the tweet and weighed by the number of followers the tweet's author has.

The sentiment and emoji dictionaries were compiled from two different sources. The emoji dictionary was obtained from previous research (kt.ijs.si/data/Emoji_sentiment_ranking/) and turned into a csv file. The sentiment library was collected from SentiWordNet (sentiwordnet.isti.cnr.it). These dictionaries contain a positivity and negativity score for each token. We use these scores when obtaining the sentiment value of a tweet.

Finally, the data included in this project are some tweets from 04/03/2017 to 04/10/2017 about five automotive industry stocks: GM, Tesla, Ford, Volkswagen, and Toyota.

***

##### File Manifest:
* app2.py
* demo.py
* EmojiSentiment.csv
* SentiWordNet.txt

***

##### Datasets:
Collection of tweets from 4/3/17 to 4/10/17 for Ford, GM, Toyota, Tesla, and Volkswagen

***

##### How To Use:
To run it on any stock ticker using the most recent tweets, run 
```sh
python demo.py [INSERT STOCK TICKER]
Example: python demo.py goog
```


To run on collected tweets run 
```sh
"python app2.py [INSERT NAME OF DIRECTORY CONTAINING TWEET FILES]/"
Example: python app2.py gm/
```

The files containing tweets need to be formatted as follows:
```sh
ID: [ID], [Tweet text, Number of followers]
Example: id: 849061127199870976 ,[u'Electric car maker Tesla, Inc. had a record quarter from January to March 2017, during which it both produced and... https://t.co/Ipoftmm3lM', 41649]
```

***

##### Authors:
Benjamin Rathi
Kevin Shah 
Yashan Thakkar
Samidha Visai

##### Acknowledgements:

We would like to thank Professor Rada Mihalcea, Michael Vander Lugt, Matthew Wiseman, and Zheng Wu for their guidance and support in EECS 486, Winter 2017. 


