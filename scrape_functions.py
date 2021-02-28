#!/usr/bin/env python
# coding: utf-8

# In[4]:


def scrape_billboard():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    url = "https://www.billboard.com/charts/hot-100"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    artist = []
    song = []
    length = len(soup.select("span.chart-element__information"))
    
    for i in range(length):
        artist.append(soup.select("span.chart-element__information__artist.text--truncate.color--secondary")[i].get_text())
        song.append(soup.select("span.chart-element__information__song.text--truncate.color--primary")[i].get_text())
    
    df_billboard = pd.DataFrame({'artist':artist, 
                                 'song': song})
    df_billboard['rank'] = np.arange(1, len(df_billboard)+1)
    
    return df_billboard


# In[5]:


def scrape_vortex():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import numpy as np
    
    url3 = 'http://www.popvortex.com/music/charts/top-100-songs.php'
    response3 = requests.get(url3)
    soup3 = BeautifulSoup(response3.content, 'html.parser')
    song3 =  []
    artist3 = []
    for i in range(1,101):
        song3.append(soup3.select(f"#chart-position-{i} > div.chart-content.col-xs-12.col-sm-8 > p > cite")[0].get_text())
        artist3.append(soup3.select(f"#chart-position-{i} > div.chart-content.col-xs-12.col-sm-8 > p > em")[0].get_text())
        
    df_vortex = pd.DataFrame({'artist':artist3, 
             'song': song3})
    df_vortex['rank'] = np.arange(1, len(df_vortex)+1)
    
    return df_vortex

