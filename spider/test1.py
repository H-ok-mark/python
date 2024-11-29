# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:42:03 2024

@author: HIIH
# WYBD8LN8US3GYG6F
"""
import requests

# replace the "WYBD8LN8US3GYG6F" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey=WYBD8LN8US3GYG6F&datatype=csv'

# Get the data
r = requests.get(url)

# Save the data as CSV (optional)
with open('stock_data.csv', 'w') as f:
    f.write(r.text)

# Print the raw CSV data
print(r.text)
