from textblob import TextBlob
from newspaper import Article
import nltk

url = "https://en.wikipedia.org/wiki/Mathematics"
article = Article(url)
article.download() # Download the article 
article.parse() # readable
article.nlp() # prep for analysis
# text = article.summary
text = article.text # get the text 
print(text)