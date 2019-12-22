import nltk
import csv
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from nltk.stem import PorterStemmer
# open the tweets stored in the result.csv file
with open("result.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        for word in row:    # read each word in each row
            word_lowercase=word.lower() # convert each word to lowercase
            white_spaces_removed = word_lowercase.strip() # remove whitespaces
            # set flag words to remove
            stop_words=set(stopwords.words('english'))
            tokens=word_tokenize(white_spaces_removed)
            # tokenize valid words not in stop words
            result = [i for i in tokens if i not in stop_words]
            print("Tokenized tweets are:")
            print(result)
            print("Stemmed tweets are")
            stemmer=PorterStemmer()  # pass the stemmer library
            print(stemmer.stem(word)) # display only unique roots, remove stems
            print(" Part of Speech tagged tweets are")
            part_of_speech=TextBlob(word) # identify part of speech
            print(part_of_speech.tags)

