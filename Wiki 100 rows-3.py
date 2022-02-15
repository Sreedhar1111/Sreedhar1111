#!/usr/bin/env python
# coding: utf-8

# In[297]:


import pandas as pd
import numpy as np
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
import urllib.request as urllib2
import time
from datetime import datetime
import json
from urllib.parse import urlencode, quote_plus
import matplotlib.pyplot as plt
import seaborn as sns


# I ended up importing a lot more things than necessary but I kept changing what I wanted to do so it is what it is

# In[298]:


TOP_API_URL = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/'              'top/en.wikipedia/all-access/2022/02/12'
    
url = TOP_API_URL

resp = urllib2.urlopen(url)
resp_bytes = resp.read()
data = json.loads(resp_bytes)
top1000 = data['items'][0]['articles']
top100 = top1000[2:102]


# My data collectino process what actually pretty simple. All I did what use the URL API to turn the top 1000 wikipedia pageviews into a JSON file. I "cleaned" up my data by making it so that my graph only used the top 100 results and I barred the first two results which are the wikipedia home page and the advanced search page. 

# In[303]:


df = pd.DataFrame(top100)
plt.figure(1)
plt.plot(df['article'], df['views'])
plt.title("Top 100 articles on wikipedia and the views they garnered on 02/12/2022")
plt.xlabel("Article")
plt.ylabel("# of Views")
plt.show()


# To be honest I almost didn't do this because of the fact that it couldn't show all the names of the 100 of the top 100 searches, but I thought that the premise was cool so I decided to do it anyway

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




