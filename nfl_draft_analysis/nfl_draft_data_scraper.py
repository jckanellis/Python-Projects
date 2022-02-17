
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define Start/Stop range
season_start = 2006
season_stop = 2021

# Grab column headers from first URL in range (assuming all column headers are the same for each dataset)
starting_url = f'https://www.pro-football-reference.com/years/{season_start}/draft.htm'

html = urlopen(starting_url)
headers_page = BeautifulSoup(html, 'html.parser')

column_headers = headers_page.findAll('tr')[1]
column_headers = [i.getText() for i in column_headers.findAll('th')]
column_headers.append('Round')
column_headers.append('Season')

stats = []

# Loop through range of URLs to grab data
for szn in range(season_start, season_stop + 1):
    url = f'https://www.pro-football-reference.com/years/{szn}/draft.htm'
    html = urlopen(url)
    stats_page = BeautifulSoup(html, 'html.parser')

    rows = stats_page.findAll('tr')[1:]

    for i in range(len(rows)):
        data = [col.getText() for col in rows[i].findAll('td')]
        rnd = [col.getText() for col in rows[i].findAll('th', {'data-stat': 'draft_round'})]
        final_data = data + rnd
        final_data.append(szn)
        stats.append(final_data)

# Transform data into dataframe
df = pd.DataFrame(stats, columns=column_headers[1:])

# Clean up null rows (this is expected from ProFootballReference)
df = df[df['Season'].notna()]