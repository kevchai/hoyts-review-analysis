import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import dateutil.parser as parser
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

review_websites = [
    "https://www.google.com/maps/place/HOYTS+Sunnybank/@-27.5712093,153.0634017,15z/data=!4m7!3m6!1s0x0:0x34896f0b2bc36a2b!8m2!3d-27.5712093!4d153.0634017!9m1!1b1"
]

reviews = []
stars = []
dates = []

for url in review_websites:
    if "google.com" in url:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(7)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        max_reviews = 1728
        num_reviews_loaded = len(reviews)

        review_pane = driver.find_element(By.CSS_SELECTOR, '.m6QErb.DxyBCb.kA9KIf.dS8AEf')
        review_pane.send_keys(Keys.END)
        print('Starting to scroll...')
        time.sleep(3)
        
        previous_height = int(review_pane.get_attribute('scrollHeight'))
        current_height = 0
        scroll_count = 0
        while current_height < previous_height:
            review_pane.send_keys(Keys.END)
            time.sleep(2)
            previous_height = int(review_pane.get_attribute('scrollHeight'))
            current_height = int(review_pane.get_attribute('scrollTop')) + int(review_pane.get_attribute('clientHeight'))
            scroll_count += 1
        input(f"Scrolled {scroll_count} times. Press Enter to continue...")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        review_data = soup.find_all('span', {'class': 'kvMYJc'})
        review_dates = soup.find_all('div', {'class': 'DU9Pgb'})
        review_content = soup.find_all('div', {'class': 'MyEned'})

        for star_data in review_data:
            review_stars = star_data.find('span', {'aria-label': True})
            stars.append(star_data.get('aria-label').replace(" stars", "").replace(" star", ""))
        for date_data in review_dates:
            review_date = date_data.find('span', {'class': 'rsqaWe'}).text
            dates.append(review_date)
        for content in review_content:
            review_text = content.find('span', {'class': 'wiI7pd'}).text
            reviews.append(review_text)

        num_reviews_loaded = len(reviews)
        print(f'Number of reviews loaded: {num_reviews_loaded}')

review_dates = []
for date in dates:
    if 'week' in date:
        if date[0] == "a":
            date = date.replace("a", "1", 1)
        num_weeks = int(date.split()[0]) * 7
        num_days = num_weeks
    elif 'hour' in date:
        num_days = 1
    elif 'day' in date:
        if date[0] == "a":
            date = date.replace("a", "1", 1)
        num_days = int(date.split()[0]) * 1
        num_days = num_days
    elif 'month' in date:
        if date[0] == "a":
            date = date.replace("a", "1", 1)
        num_months = int(date.split()[0]) * 30
        num_days = num_months
    elif 'year' in date:
        if date[0] == "a":
            date = date.replace("a", "1", 1)
        num_years = int(date.split()[0]) * 365
        num_days = num_years
    else:
        review_date = parser.parse(date)
    current_date = pd.datetime.now()
    review_date = current_date - pd.Timedelta(days=num_days)
    review_date = review_date.strftime("%Y/%m")
    review_dates.append(review_date)

reviews_df = pd.DataFrame(reviews, columns=['review'])
reviews_df['stars'] = stars
reviews_df['date'] = review_dates

sia = SentimentIntensityAnalyzer()
sentiments = []
for review in reviews:
    sentiment = sia.polarity_scores(review)
    sentiments.append(sentiment)

sentiments_df = pd.DataFrame(sentiments, columns=['neg', 'neu', 'pos', 'compound'])
merged_df = pd.merge(reviews_df, sentiments_df, left_index=True, right_index=True)
print(merged_df)

merged_df.to_csv('reviews.csv', index=False)
