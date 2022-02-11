import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from draft_data_scraper import *

# Call web crawler
exec(open("draft_data_scraper.py").read())

# Clean up player names
df['Player'] = df['Player'].str.replace('HOF', '')

# Convert Pro Bowl values to integers
df['PB'] = pd.to_numeric(df['PB'])

pro_bowls = df.groupby('Round')['PB'].sum()

# Plot number of Pro Bowlers by draft round
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
round = np.arange(1, 8, 1).tolist()
ax.bar(round, pro_bowls)
plt.show()
