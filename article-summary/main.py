import tkinter as tk
from textblob import TextBlob
import nltk
from newspaper import Article

url = "https://edition.cnn.com/2025/10/13/tech/openai-broadcom-power"
article = Article(url)
article.download()
article.parse()
article.nlp()

print("Title:", article.title)
print("Authors:", article.authors)
print("Publication Date:", article.publish_date)
print("Summary:", article.summary)
