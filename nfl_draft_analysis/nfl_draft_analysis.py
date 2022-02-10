import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from draft_data_scraper import *

# Call web crawler
exec(open("draft_data_scraper.py").read())

# Clean up player names
df['Player'] = df['Player'].str.replace('HOF', '')