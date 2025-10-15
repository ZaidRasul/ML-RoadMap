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
print(f"Subjectivity: {"subjective" if sentiment.subjectivity > 0.3 else "objective"}")

# GUI to display the article summary and sentiment
root = tk.Tk()
root.title("Article Summary and Sentiment Analysis")
root.geometry("1200x600")

# Title
tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state = "disabled", bg="#dddddd")
title.pack()

# Authors
authors_label = tk.Label(root, text="Authors")
authors_label.pack()

authors = tk.Text(root, height=1, width=140)
authors.config(state = "disabled", bg="#dddddd")
authors.pack()
# Publication Date
date_label = tk.Label(root, text="Publication Date")
date_label.pack()

date = tk.Text(root, height=1, width=140)
date.config(state = "disabled", bg="#dddddd")
date.pack()

# Summary
summary_label = tk.Label(root, text="Summary")
summary_label.pack()

summary = tk.Text(root, height=10, width=140)
summary.config(state = "disabled", bg="#dddddd")
summary.pack()

# Sentiment
sentiment_label = tk.Label(root, text="Sentiment")
sentiment_label.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state = "disabled", bg="#dddddd")
sentiment.pack()

# enter URL
url_label = tk.Label(root, text="URL")
url_label.pack()

url = tk.Text(root, height=1, width=140)
url.pack()

btn = tk.Button(root, text="Analyze", command=lambda: Anal(url.get("1.0", "end-1c"), title, authors, date, summary, sentiment))
btn.pack()

root.mainloop()