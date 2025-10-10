from textblob import TextBlob


'''
from newspaper import Article

url = "https://www.cnbc.com/2020/04/22/recession-depth-will-be-much-worse-than-2007-2009-lakshman-achuthan.html"
article = Article(url)
article.download() # Download the article 
article.parse() # readable
article.nlp() # prep for analysis
# text = article.summary
text = article.text # get the text 
print(text)''' 

with open('NNs/sentiment_analysis_text.txt', 'r') as file:
    text = file.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)