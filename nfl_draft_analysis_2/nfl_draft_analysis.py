import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nfl_draft_web_crawler import *

# Call web crawler
exec(open("nfl_draft_web_crawler.py").read())

# Clean up player names
df['Player'] = df['Player'].str.replace('HOF', '')

# Convert Pro Bowl values to integers
df['PB'] = pd.to_numeric(df['PB'])

pro_bowls = df.groupby('Round')['PB'].sum()

# Plot number of Pro Bowlers by draft round
round = np.arange(1, 8, 1).tolist()

plt.bar(round, pro_bowls)
plt.xlabel('Draft Round')
plt.ylabel('# of Pro Bowls')
plt.title(f'Pro Bowls by Draft Round {season_start} - {season_stop}')
plt.show()

# Potential questions:
# What % of players drafted in the top 10 actually make a Pro Bowl
# How many #1 overall picks never make it to the Pro Bowl