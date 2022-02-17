import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nfl_draft_data_scraper import *

# Call web crawler
exec(open("nfl_draft_data_scraper.py").read())

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