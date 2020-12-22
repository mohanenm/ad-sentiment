from csv_to_dataframe import *

cols = tweet_df.columns
# Create a new concatenated DataFrame
df3 = pd.concat([tweet_df['sentiment'].value_counts(normalize=True)])
df3.to_csv("results.md", sep="\n", index=False)

#TODO: add correct separators so it transfers to md elegantly