import numpy as np
import pandas as pd
import random
import spacy
from textblob import TextBlob

# Reads in .csv file, selects relevant columns, drops null values and selects just the review text column.
amazon = pd.read_csv("amazon_product_reviews.csv")
cleaned = amazon[['reviews.text','reviews.title','reviews.username']]
cleaned.dropna(inplace=True, axis=0)
text = cleaned['reviews.text']

# Preprocess function tokenizes, lemmatizes, converts to lower,
# removes stop words and punctuation and returns string of processed tokens.
nlp = spacy.load('en_core_web_md')
def preprocess(text):
    doc = nlp(text.lower().strip())
    processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

    return ' '.join(processed)

# Adds column of processed reviews to data frame.
cleaned['processed.text'] = cleaned['reviews.text'].apply(preprocess)

# Sentiment analysis function uses textblob to analyse sentiment
# and returns polarity.
def analyze_polarity(text):
    doc = nlp(text)

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    return polarity

# Analyses polarity of each processed review and adds assigned sentiment to sentiments list.
sentiments = []
for item in cleaned['processed.text']:
    polarity_score = analyze_polarity(item)

    if polarity_score > 0.8:
        sentiment = 'very positive'
    elif polarity_score > 0.5:
        sentiment = 'positive'
    elif polarity_score > 0.2:
        sentiment = 'somewhat positive'
    elif polarity_score >= 0:
        sentiment = 'neutral'
    elif polarity_score < 0:
        sentiment = 'negative'

    sentiments.append(sentiment)

# Counts positive, negative and neutral sentiments, uses length of sentiments list
# to calculate percentages of each.
very_positive_count = sentiments.count('very positive')
positive_count = sentiments.count('positive')
somewhat_positive_count = sentiments.count('somewhat positive')
neutral_count = sentiments.count('neutral')
negative_count = sentiments.count('negative')

total = len(sentiments)
very_positive_perc = (very_positive_count / total) * 100
positive_perc = (positive_count / total) * 100
somewhat_positive_perc = (somewhat_positive_count / total) * 100
neutral_perc = (neutral_count / total) * 100
negative_perc = (negative_count / total) * 100

print(f"Very positive: {very_positive_perc:.2f}%")
print(f"Positive: {positive_perc:.2f}%")
print(f"Somewhat positive: {somewhat_positive_perc:.2f}%")
print(f"Negative percentage: {negative_perc:.2f}%")
print(f"Neutral percentage: {neutral_perc:.2f}%")

# Assigns random integer to select sample reviews, using length of sentiments list to define range.
sample_1 = random.randint(0, total-1)
sample_2 = random.randint(0, total-1)

# Prints sample reviews text and polarity.
print("Sample 1 text: ", cleaned['reviews.text'][sample_1])
print("Sample 1 polarity: ", analyze_polarity(cleaned['reviews.text'][sample_1]))
print("Sample 2 text: ", cleaned['reviews.text'][sample_2])
print("Sample 2 polarity: ", analyze_polarity(cleaned['reviews.text'][sample_2]))

# Finds similarity between sample reviews.
similarity = nlp(cleaned['processed.text'][sample_1]).similarity(nlp(cleaned['processed.text'][sample_2]))
print("Similarity between Samples 1 and 2: ", similarity)
