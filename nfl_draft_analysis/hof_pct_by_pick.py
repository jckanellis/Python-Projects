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

# Count number of draft picks per pick sequence
pick_count = df.groupby('Pick')['AP1'].count()

# Count number of HOF draft picks per pick sequence (HOF defined as having >= 3 First Team All Pro (AP1))
hof_pick_count = df[df['AP1'] >= 3]
hof_pick_count = hof_pick_count.groupby('Pick')['PB'].count()

# Combine series
agg_df = pd.concat([pick_count, hof_pick_count], axis=1)

# Calculate Pro Bowl draft %
agg_df['HOF_Pct'] = (hof_pick_count / pick_count) * 100

# Plot
index = len(agg_df)
round = np.arange(1, index + 1, 1).tolist()

plt.bar(round, agg_df['HOF_Pct'])
plt.title(f'Hall of Fame Draft % by Pick {season_start} - {season_stop} Seasons')
plt.xlabel('Pick')
plt.show()

test_df = df[df['Pick'] == 5]