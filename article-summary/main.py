import tkinter as tk
from textblob import TextBlob as tb
import nltk
from newspaper import Article

nltk.download('punkt')

url = "https://edition.cnn.com/2025/10/13/tech/openai-broadcom-power"
article = Article(url)
article.download()
article.parse()
article.nlp()

print("Title:", article.title)
print("Authors:", article.authors)
print("Publication Date:", article.publish_date)
print("Summary:", article.summary)

# sentiment analysis gives polarity and subjectivity
# polarity: -1 (negative) to 1 (positive)
# subjectivity: 0 (objective) to 1 (subjective) [measure of personal opinion]
sentiment = tb(article.text).sentiment
print("Sentiment:", sentiment)
print(f"Polarity: {"positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"}")
print(f"Subjectivity: {"subjective" if sentiment.subjectivity > 0.5 else "objective"}")