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

# custom_pick = df[df['Pick'] == 5]

pro_bowls = df.groupby('Round')['PB'].sum()

# Plot number of Pro Bowlers by draft round
# round = np.arange(1, 8, 1).tolist()
#
# plt.bar(round, pro_bowls)
# plt.xlabel('Draft Round')
# plt.ylabel('# of Pro Bowls')
# plt.title(f'Pro Bowls by Draft Round {season_start} - {season_stop}')
# plt.show()

# Plot number of Pro Bowls by pick
# pick = np.arange(1,51,1).tolist()
# filtered_df = df[df['Pick'] <= 50]
# pro_bowls_pick = filtered_df.groupby('Pick')['PB'].mean()
# pro_bowls_pick.sort_index()
#
# plt.bar(pick, pro_bowls_pick)
# plt.xlabel('Pick')
# plt.ylabel('# of Pro Bowls')
# plt.title(f'Pro Bowls by Pick {season_start} - {season_stop}')
# plt.show()

# Picks with at least 1 Pro Bowler
# filtered_df = df[df['PB'] > 0]
# pro_bowls_pick = filtered_df.groupby('Pick')['PB'].count()
# pro_bowls_pick = pro_bowls_pick[pro_bowls_pick > 1]
# index = len(pro_bowls_pick.index)
# pick = np.arange(1,index + 1,1).tolist()
#
# plt.bar(pick, pro_bowls_pick)
# plt.xlabel('Pick')
# plt.ylabel('# of Picks w/ Pro Bowl')
# plt.title(f'Pro Bowl Players by Pick {season_start} - {season_stop}')
# plt.show()

# Pro Bowl % by Pick
# df = df[df['Pick'] >= df['Round']]
# pick_count = df.groupby('Pick')['PB'].count()
# only_pro_bowlers = df[df['PB'] > 0]
# pro_bowl_count = only_pro_bowlers.groupby('Pick')['PB'].count()
#
# merge = pd.concat([pick_count, pro_bowl_count], axis=1)
# merge['Pro_Bowl_Pct'] = (pro_bowl_count / pick_count) * 100
# merge = merge.fillna(0)
#
# index = len(merge)
# pick = np.arange(1,index+1,1).tolist()
#
# plt.bar(pick, merge['Pro_Bowl_Pct'])
# plt.xlabel('Pick')
# plt.ylabel('% of Pro Bowlers')
# plt.title(f'Pro Bowl % by Pick {season_start} - {season_stop}')
# plt.show()

# Pro Bowl % by Round
df = df[df['Pick'] >= df['Round']]
round_count = df.groupby('Round')['AP1'].count()
only_pro_bowlers = df[df['AP1'] > 3]
pro_bowl_count = only_pro_bowlers.groupby('Round')['AP1'].count()

merge = pd.concat([round_count, pro_bowl_count], axis=1)
merge['Pro_Bowl_Pct'] = (pro_bowl_count / round_count) * 100
merge = merge.fillna(0)

index = len(merge)
round = np.arange(1, index + 1, 1).tolist()

plt.bar(round, merge['Pro_Bowl_Pct'])
plt.xlabel('Round')
plt.ylabel('% of HOF')
plt.title(f'HOF % by Round {season_start} - {season_stop}')
# ax = plt.gca()
# ax.set_ylim([0,50])
plt.show()

# Draft Insights:
# Probability of drafting a Pro Bowler (by pick/round)
# Probability of drafting a HOF (by pick/round)
# League-wide drafting ability
# Drafting ability by team
