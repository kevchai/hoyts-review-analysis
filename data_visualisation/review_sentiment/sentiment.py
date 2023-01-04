import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../reviews-2022.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')
df.set_index('date', inplace=True)
df = df.resample('M').mean(numeric_only=True)

plt.figure(figsize=(16,8))

df['compound'].plot()

plt.xticks(df.index, df.index.strftime('%m/%Y'))
plt.xticks(rotation=90)

plt.title("Sentiment over Time for year 2022")
plt.xlabel("Period")
plt.ylabel("Compound Sentiment Score")
plt.ylim(0, 1)
plt.grid(True, color='#c2c2c2')
plt.savefig('output/sentiment_over_time.png')
