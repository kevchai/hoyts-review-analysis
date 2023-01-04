import pandas as pd
import matplotlib.pyplot as plt

# Read the reviews.csv file into a pandas DataFrame
df = pd.read_csv('../../reviews-2022.csv')

# Convert the 'date' column to datetime objects
df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(by='date')

# Set the index of the DataFrame to the date column
df.set_index('date', inplace=True)

# Resample the DataFrame by month
df = df.resample('M').mean(numeric_only=True)

plt.figure(figsize=(16,12))
plt.grid(True, color='#c2c2c2')

# Create a bar chart showing the distribution of review stars over time
df.plot.scatter(x=df.index, y='stars')

# Format the x axis labels as month/year
plt.xticks(df.index, df.index.strftime('%m/%Y'))

plt.xticks(rotation=90)

# Save the bar chart to an image file
plt.title('Review Stars Over Time for year 2022')
plt.xlabel("Period")
plt.ylabel('Review Stars')
plt.ylim(0, 5)
plt.savefig('output/stars_over_time.png')

