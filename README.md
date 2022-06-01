# nlp-demo
Simple demo that does the following:
GetTweets: 
  Pull tweets from a single Twitter account
  Cleans the tweets dataset
  Creates a wordcloud to show common words
  **Output Files:** 
    tweets.csv: dataframe of tweets, including username, time
    tweets.txt text file of cleaned tweet data (only tweet data is included)
    wordcloud.png
    
 ClusterTweets:
  Creates a word2vec model from tweets
  Creates a cluster model (unsupervised) to organize tweets into 2 clusters
  **Output:**
    Centroid of each cluster (printout from code)
    Top 10 positive terms (printout from code)
    Top 10 negative terms (printout from code)
