import requests 
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np




url = 'http://www.hannovermesse.de/en/exhibitors/sitemap.xml'
res = requests.get(url)


#%%
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('url')


#%%
a = pd.DataFrame([str(i).split('loc')[1][1:-2] for i in table], columns=['url'])

print(a.head())
a.to_csv('HSM_2018.csv')