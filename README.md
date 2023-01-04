# Hoyts' Google Review Analysis
This is a Python script that scrapes customer review data from Google, preprocess the data and generate wordclouds and a sentiment analysis line chart.

### Data
The script will collect customer Google review data on Hoyts Sunnybank, with each review containing a rating (on a scale of 1 to 5 stars), a review text, and the review date, stored in a CSV file.

### Data Preprocessing
Before analyzing the data, some preprocessing was performed to clean and prepare the data for analysis. This included:

- Removing any null or empty values from the data
- Converting the date column to datetime objects
- Sorting the data by date
- Setting the index of the DataFrame to the date column

### Data Visualisation
The following visualisations were created to help understand and analyze the customer reviews:

#### Wordcloud
Wordclouds were created to show the most commonly used words in the review text for 1 to 3 stars reviews and 4 to 5 stars reviews. Stop words, such as common pronouns and prepositions, were removed to better understand the content of the reviews.

#### Review Sentiment Over Time
Using natural language processing, each review text was analysed and given a review sentiment score. A line plot was created to show the distribution of review sentiment over time. This allows us to see if there are any trends or patterns in the sentiment over time.
