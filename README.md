# Twitter-Scraping-and-Sentiment-Analysis
Tweets retrieved about US mobile carrier sentiments


## Summary

Twitter is among the most popular social media /microblogging platforms that has become a global phenomenon since its inception in 2006. With 320 million daily users and 500 million tweets sent each day, it is also one of the largest text data repositories. Users convey how they are feeling and what they are doing in the form of updates ranging from 1-280 characters for all languages except for Korean, Japanese and Chinese.  


## Purpose

Using sentiment analysis, an analysis of public mood of the four biggest United States carriers  T-Mobile, AT&T, Sprint, and Verizon will be gauged.




## Objectives

1.	Web scrape Twitter using Python 3 tools
2.	Preprocessing of text
3.	Tokenization of tweets using NLTK
4.	 Data Cleaning using NLTK and regular expressions
5.	Data visualization of mood polarity


## Implementation


The file twitter_sent_model.py is responsible for connecting to the Twitter API Tweepy and retrieving the tweets using a combination of the consumer_key, consumer_secret_key, accessToken, accessTokenSecret for authentication purposes. Two search terms are given as input: one for the string input of the carrier and the other an integer value for the number of tweets required to analyze. The twitter_sent_model.py uses a single class called SentimentAnalysis and four objects for each of the United States carriers call the class methods. Initially, two empty lists are created to store the tweets and their text in the _init_ function. Consequently, the next function is to retrieve the tweets by authenticating the twitter developer credentials and writing the tweets to a csv file.

Polarity of each tweet is used through the TextBlob library which efficiently calculates the polarity as a float number. Here, we pass the tweet.text which we have initialized in the _init_ function as analysis=TextBlob(tweet.text)and determine polarity using the analysis.sentiment.polarity. Likewise, a series of conditional statements will be used to determine if the tweet is negative, neutral or positive (neutral=0.0, positive>0.0, negative<0.0). Finally, the polarity will be calculated as a percentage of every polarity/number of tweets and plotted as a graph in the displayGraph function and labelled accordingly with negative, positive and neutral having their own respective colors.

In contrast, nlp.py consists of importing several nltk (Natural Language Tool Kit) libraries and the TextBlob libraries. Each row of the csv file containing the stored tweets is read, converted to all lower-case, and white-spaces are removed. White spaces are simply deleted by using the built-in Python strip() function. Following this, stopwords from the nltk corpora are identified and for every word in the tweet that is part of the stopwords list is removed. Next, the PorterStemmer library is utilized to keep only root words and remove all repetitive stem words. At last, the part-of-speech of each tweet word is tagged through Textblob and printed on a separate line.


## Results

According to the results of the twitter web scraping, the carrier with the most positive sentiment is AT&T at 45.9% positive, followed closely by Sprint at 41.3% positive, Verizon with 39.4% and T-Mobile with the least positive polarity at 33.3%.


## Limitations

Every web scraping and analysis method has its shortcomings including twitter scraping and sentiment analysis. Among these are Tweepy’s security measures. Since Twitter strives to have user privacy is essential to its company policies, Twitter only allows scraping of tweets for developer accounts. Obtaining a Twitter developer account can be quite a hassle as Twitter requires an existing account, a detailed summary of how the API will be used, and a wait period of 2-3 days. Often, Twitter can reject a developer account on the grounds that the application is a threat to users’ privacy.

Additionally, complications arose when scraping the tweets and performing NLP preprocessing and sentiment analysis. Twitter only allows 2000.tweets to be collected per day on the same accessToken. Accordingly, the collection of tweets was done on two separate days as 1000 tweets were needed from every mobile carrier. Upon, gathering the tweets, polarity of each tweet can sometimes be skewed by the fact that some tweets consist of non-textual information like emojis, GIFs, videos, and images. Subsequently, each tweet in Tweepy is written cell-wise to a csv file even if in the program it is written to the csv file by row. This negates the use of the pandas library as data frames for NLP preprocessing are generally built row-wise and sometimes column-wise.



## Scope of Project

1.	 Real time analysis and identification of company related problems
2.	Customer feedback
3.	Product improvement
4.	Scalability
