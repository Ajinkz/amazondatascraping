# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:25:50 2022
@author: ajinkya
"""

import json
from pandas import json_normalize
import pandas as pd
import requests


keyword = "iphone"
#pg_num = 3

# set up the request parameters
params = {
  'api_key': '0B2B152AB0AC491990F021C8A2D48DFB',
  'type': 'search',
  'amazon_domain': 'amazon.com',
  'search_term': keyword,
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# print the JSON response from Rainforest API
#print(json.dumps(api_result.json()))
print(api_result.json()["request_info"])

results = api_result.json()["search_results"]

df = json_normalize(results)
#df.head()

#cols = ['position', 'title', 'asin', 'link', 'categories', 'image', 'is_prime','rating', 'ratings_total', 'price.value']
#df = df[cols]

df.to_csv(keyword+".csv", index=False)
print("CSV saved successfully !")


