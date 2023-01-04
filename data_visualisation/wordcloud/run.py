from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

df = pd.read_csv('../../reviews.csv')

filtered_reviews = []
filtered_reviews_1_3_stars = []
filtered_reviews_4_5_stars = []

reviews = df['review'].tolist()
reviews_1_3_stars = df['review'].tolist()
reviews_4_5_stars = df['review'].tolist()

stop_words = stopwords.words('english')
stop_words.extend(['cinema', 'cinemas', 'cinemas.', '.', 'movie', 'hoyts', 'really', 'going', 'always', 'good', 'nice', 'place', 'great', 'love', 'loved', 'every', 'seat', 'movie'])

for review in df[df['stars'].isin([1, 2, 3])]['review']:
    if isinstance(review, str):
        words = review.split()
        for word in words:
            word = word.lower()
            if word not in stop_words:
                filtered_reviews_1_3_stars.append(word)

for review in df[df['stars'].isin([4, 5])]['review']:
    if isinstance(review, str):
        words = review.split()
        for word in words:
            word = word.lower()
            if word not in stop_words:
                filtered_reviews_4_5_stars.append(word)

for review in reviews:
    if isinstance(review, str):
        words = review.split()
        for word in words:
            word = word.lower()
            if word not in stop_words:
                filtered_reviews.append(word)

reviews_string = " ".join([review for review in reviews if isinstance(review, str) or isinstance(review, int)])
filtered_reviews_1_3_stars_string = " ".join(filtered_reviews_1_3_stars)
filtered_reviews_4_5_stars_string = " ".join(filtered_reviews_4_5_stars)
filtered_reviews_string = " ".join(filtered_reviews)

plt.figure(figsize=(16,8))

wordcloud = WordCloud(width=500, height=700, background_color='white').generate(filtered_reviews_string)
wordcloud_1_3_stars = WordCloud(width=500, height=700, background_color='white').generate(filtered_reviews_1_3_stars_string)
wordcloud_4_5_stars = WordCloud(width=500, height=700, background_color='white').generate(filtered_reviews_4_5_stars_string)

wordcloud.to_file('wordcloud.png')
wordcloud_1_3_stars.to_file('wordcloud_1_3_stars.png')
wordcloud_4_5_stars.to_file('wordcloud_4_5_stars.png')