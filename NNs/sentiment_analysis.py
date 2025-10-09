from textblob import TextBlob
from newspaper import Article
import nltk

url = "https://en.wikipedia.org/wiki/Mathematics"
article = Article(url)
nltk.download('punkt')
nltk.download('punkt_tab')
article.download() # Download the article 
article.parse() # readable
article.nlp() # prep for analysis

text = article.text # get the text 
print(text)