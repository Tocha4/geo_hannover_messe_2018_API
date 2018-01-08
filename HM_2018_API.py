import requests
import pandas as pd
from bs4 import BeautifulSoup as bs



url = 'http://www.hannovermesse.de/en/exhibitors/sitemap.xml'
res = requests.get(url)

for i in res.headers:
    print('{}: {}'.format(i,res.headers[i]))

soup = bs(res.content, 'html.parser')
url_list = soup.find_all('loc')
df = pd.DataFrame([str(i).strip('loc></loc') for i in url_list])
print(df.head())
#%%

def checking(res):
    if res == None:
        res = 'NaN'
    else: pass
    return res
class TN():
    def __init__(self):
        self.text = '\tNo tel_number\n'
        
    
def get_data(df):
    
    data = {'name':[],
           'street':[],
           'city':[],
            'zip_code':[],
           'country':[],
           'tel_number':[],
           'website':[],}
    for n,i in enumerate(df[0]):
        res = requests.get(i)
        soup = bs(res.content, 'html.parser')
        
        name = soup.find('h3', {'itemprop': 'companyName'}).text
        street = soup.find('div', {'itemprop':'street'}).text
        city = soup.find('div', {'itemprop':'city'}).text
        country = soup.find('div', {'itemprop':'country'}).text.split('\n')[0]
        tel_number = [i.text.strip('\t\n') for i in [soup.find('a', {'class':'tel-number'}), TN()] if i != None][0]
        website = [i['href'] for i in [soup.find('a', {'class': 'textLink icon-external-link'}), 
                                       {'href': 'NaN'}] if i != None][0]
        print(website)
        data['name'].append(name)
        data['street'].append(street)
        data['city'].append(city.split(' ')[1])
        data['zip_code'].append(city.split(' ')[0])
        data['country'].append(country)
        data['tel_number'].append(tel_number)
        data['website'].append(website)
        



    ddf = pd.DataFrame(data)
    return ddf
#%%           
ddf = get_data(df)
ddf.head()
#%%

ddf.to_csv('exhibitors.csv')