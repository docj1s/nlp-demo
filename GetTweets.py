import snscrape.modules.twitter as sntwitter
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
token = WordPunctTokenizer()

import string
import re

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

tweets_list1 = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:LeBatardShow').get_items()):
    if i>1000:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

tweets_df1 = pd.DataFrame(tweets_list1, columns=['DateTime', 'Tweet Id', 'Text', 'Username'])

print(tweets_df1.head())
print(tweets_df1.tail())


def cleaning_URLs(text):
    return re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)

tweets_df1['Text']= tweets_df1['Text'].apply(lambda x: cleaning_URLs(x))

#remove @mentions and hashes
def clean_mentions_and_hashes(text):
    re_list = ['@[A-Za-z0-9_]+', '#']
    combined_re = re.compile('|'.join( re_list))
    return re.sub(combined_re, '', text)

tweets_df1['Text']= tweets_df1['Text'].apply(lambda x: clean_mentions_and_hashes(x))

stopwords_list = stopwords.words('english')

from nltk.corpus import stopwords
", ".join(stopwords.words('english'))

english_punctuations = string.punctuation
punctuations_list = english_punctuations
def cleaning_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

tweets_df1['Text']= tweets_df1['Text'].apply(lambda x: cleaning_punctuations(x))

def cleaning_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)

#tweets_df1['Text']= tweets_df1['Text'].apply(lambda x: cleaning_repeating_char(x))

def cleaning_email(text):
    return re.sub('@[^\s]+', ' ', text)

tweets_df1['Text']= tweets_df1['Text'].apply(lambda x: cleaning_email(x))



def beautify(text):
    bs = BeautifulSoup(text, 'lxml')
    return bs.get_text()

tweets_df1['Text']= tweets_df1['Text'].apply(lambda x: beautify(x))
tweets_df1['Text']= tweets_df1['Text'].str.lower()

print(tweets_df1.head())
print(tweets_df1.tail())


def final_clean(t):
    words = token.tokenize(t)
    result_words = [x for x in words if len(x) > 2]
    return (" ".join(result_words)).strip()

cleaned_tweets = []
for i in range(0, tweets_df1.shape[0]):
    cleaned_tweets.append(final_clean((tweets_df1.loc[i, 'Text'])))

stopwords = set(STOPWORDS)

string = pd.Series(cleaned_tweets).str.cat(sep=' ')

wordcloud = WordCloud(width=1600, height=800, max_font_size=200, max_words=50, collocations=False, background_color="black").generate(string)

plt.figure(figsize=(40,30))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig('wordcloud.png')


