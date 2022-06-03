import pandas as pd 
import numpy as np 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("/home/rjones/twitter/PlayoffTweets.csv", delimiter="\t")

df['Text'] = df['Text'].str.lower()

teamName = "heat"
print(df.Text.str.contains(teamName).sum())
print(df.Text.str.contains("heat").sum())
print(df.Text.str.contains("panthers").sum())


def computeSentiment(df):
    analyzer = SentimentIntensityAnalyzer()
    df['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df['Text']]
    df['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df['Text']]
    df['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df['Text']]
    df['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df['Text']]

    return df

df_heat = df.query('Text.str.contains("heat")')
df_heat = computeSentiment(df_heat)

df_panthers = df.query('Text.str.contains("panthers")')
df_panthers = computeSentiment(df_panthers)

df_marlins = df.query('Text.str.contains("marlins")')
df_marlins = computeSentiment(df_marlins)

df_dolphins = df.query('Text.str.contains("dolphins")')
df_dolphins = computeSentiment(df_dolphins)


#df_heat['compound'] = [analyzer.polarity_scores(x)['compound'] for x in df_heat['Text']]
#df_heat['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df_heat['Text']]
#df_heat['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df_heat['Text']]
#df_heat['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df_heat['Text']]

def printSentiment(df, team):
    avg_compound = np.average(df['compound'])
    avg_neg = np.average(df['neg']) * -1  # Change neg value to negative number for clarity
    avg_neu = np.average(df['neu'])
    avg_pos = np.average(df['pos'])

    # Counting number of tweets
    count = len(df.index)

    # Print Statements
    print(count ,  "tweets on the " + team, end='\n*')
    print("Positive Sentiment:", '%.2f' % avg_pos, end='\n*')
    print("Neutral Sentiment:", '%.2f' % avg_neu, end='\n*')
    print("Negative Sentiment:", '%.2f' % avg_neg, end='\n*')
    print("Compound Sentiment:", '%.2f' % avg_compound, end='\n\n')

count = len(df.index)
print("Since the start of April, there has been ", count ,  "tweets.", end='\n')
print(end='\n')

printSentiment(df_heat, "Miami Heat")
printSentiment(df_panthers, "Florida Panthers")
printSentiment(df_marlins, "Florida Marlins")
printSentiment(df_dolphins, "Miami Dolphins")


