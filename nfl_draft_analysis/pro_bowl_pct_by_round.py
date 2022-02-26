import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nfl_draft_data_scraper import *

# Call web crawler
exec(open("nfl_draft_data_scraper.py").read())

# Clean up player names
df['Player'] = df['Player'].str.replace('HOF', '')

# Convert Pro Bowl & Pick values to integers
df['PB'] = pd.to_numeric(df['PB'])
df['Pick'] = pd.to_numeric(df['Pick'])
df['Round'] = pd.to_numeric(df['Round'])
df['AP1'] = pd.to_numeric((df['AP1']))

# Count number of draft picks per round
pick_count = df.groupby('Round')['PB'].count()

# Count number of Pro Bowl draft picks per round
pro_bowl_pick_count = df[df['PB'] > 0]
pro_bowl_pick_count = pro_bowl_pick_count.groupby('Round')['PB'].count()

# Combine series
agg_df = pd.concat([pick_count, pro_bowl_pick_count], axis=1)

# Calculate Pro Bowl draft %
agg_df['PB_Pct'] = (pro_bowl_pick_count / pick_count) * 100

# Plot
index = len(agg_df)
round = np.arange(1, index + 1, 1).tolist()

plt.bar(round, agg_df['PB_Pct'])
plt.title(f'Pro Bowl Draft % by Round {season_start} - {season_stop} Seasons')
plt.xlabel('Round')
plt.show()