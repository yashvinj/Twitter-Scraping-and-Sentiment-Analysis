import tweepy # Twitter API
import csv # comma separated values
import re # regular expression library
from textblob import TextBlob  # sentiment analysis library
import matplotlib.pyplot as plt # graph library


# sentiment analysis class to ensure abstraction and other oops features
class SentimentAnalysis:

    # initialize lists to store retrieved tweets and  their text
    def __init__(self):
        self.tweets = []
        self.tweetText = []

    def retrieveTweets(self):
        # authenticating the API access using private keys and tokens
        consumerKey = 'fnRrf9PAHRhAtpC3KsQBPDVRQ'
        consumerSecret = 'XDhRNPb2nstJl2I1o0ekDlakZfA1c7Y80vny8KIoAS0SUcB4gC'
        accessToken = '198660393-coCgHhpVCIM2zmgokdHYOW9ENlk7IrGyUXDcTK5w'
        accessTokenSecret = 'OMZdI9l0wUfTIsJ9jQostd6lj0uho0x80ouYipGnNpqPP'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        # input for term to be searched and how many tweets to search
        searchTerm = input("Enter the US carrier to perform sentiment analysis: ")
        number_of_tweets = int(input("Enter how many tweets to search: "))

        # searching for tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang =
        "en").items(number_of_tweets)

        # Open/create a file to append data to
        csvFile = open('result.csv', 'a')

        # Use csv writer
        csvWriter = csv.writer(csvFile)
        # creating some variables to store info
        polarity = 0
        positive = 0
        negative = 0
        neutral = 0

        # iterating through tweets fetched
        for tweet in self.tweets:
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            # print (tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later
            if (analysis.sentiment.polarity == 0):  # adding reaction of how
                # people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0):
                positive += 1
            elif (analysis.sentiment.polarity < 0):
                negative += 1

        # Write to csv and close csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # finding average of how people are reacting
        positive = self.percentage(positive, number_of_tweets)
        negative = self.percentage(negative, number_of_tweets)
        neutral = self.percentage(neutral, number_of_tweets)

        # finding average reaction
        polarity = polarity / number_of_tweets

        # printing out data
        print("Sentiment Analysis " + searchTerm + " by analyzing " +
              str(number_of_tweets) + " tweets.")
        print()
        print("Average Polarity ")

        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0):
            print("Positive")
        elif (polarity < 0):
            print("Negative")
        print()
        print("Statistics: ")
        print(str(positive) + "% people thought it was positive")
        print(str(negative) + "% people thought it was negative")
        print(str(neutral) + "% people thought it was neutral")

        self.displayGraph(positive,negative,neutral, searchTerm, number_of_tweets)


    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

    # function to display the graph using matplotlib
    def displayGraph(self, positive, negative, neutral, searchTerm,
                     noOfSearchTerms):
        labels = ['Positive [' + str(positive) + '%]',
                  'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]']
        sizes = [positive, neutral, negative]
        colors = ['yellow','blue','red']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.title('Sentiment Analysis of ' + searchTerm + ' by analyzing '
                  + str(noOfSearchTerms) + ' Tweets.')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()


# main function to call the 4 carrier objects
if __name__== "__main__":
    carrier1 = SentimentAnalysis()
    carrier1.retrieveTweets()
    carrier2 = SentimentAnalysis()
    carrier2.retrieveTweets()
    carrier3 = SentimentAnalysis()
    carrier3.retrieveTweets()
    carrier4 = SentimentAnalysis()
    carrier4.retrieveTweets()