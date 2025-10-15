import tkinter as tk
from textblob import TextBlob as tb
import nltk
from newspaper import Article

def Analyze():
    
    url = url_text.get("1.0", "end")
    
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    #when the text box is disabled, we need to enable it to insert text and then disable it again
    title.config(state="normal")
    authors.config(state="normal")
    date.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")
    subjectivity.config(state="normal")

    # Clear old text
    title.delete("1.0", "end")
    authors.delete("1.0", "end")
    date.delete("1.0", "end")
    summary.delete("1.0", "end")
    sentiment.delete("1.0", "end")
    subjectivity.delete("1.0", "end")

    # intsert new text
    title.insert("1.0", article.title)
    authors.insert("1.0", ", ".join(article.authors))
    date.insert("1.0", article.publish_date)
    summary.insert("1.0", article.summary)
    sentiment.insert("1.0", f"Polarity: {"positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"}")
    subjectivity.insert("1.0", f"Subjectivity: {"subjective" if sentiment.subjectivity > 0.3 else "objective"}")

    #Disable the text box
    title.config(state="disabled")
    authors.config(state="disabled")
    date.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")
    subjectivity.config(state="disabled")

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

# Subjectivity
subjectivity_label = tk.Label(root, text="Subjectivity")
subjectivity_label.pack()

subjectivity = tk.Text(root, height=1, width=140)
subjectivity.config(state = "disabled", bg="#dddddd")
subjectivity.pack()

# enter URL
url_label = tk.Label(root, text="URL")
url_label.pack()

url_text = tk.Text(root, height=1, width=140)
url_text.pack()

btn = tk.Button(root, text="Analyze", command=Analyze)
btn.pack()

root.mainloop()