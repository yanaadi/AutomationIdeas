#!/usr/bin/env python
# coding: utf-8

# In[146]:


import requests,json,webbrowser
    
api_key = 'AIzaSyCloDNAk4uGQfw8BKmi8fMdGQiOSaF7rwA'

ch_id = 'UCXuqSBlHAE6Xw-yeJA0Tunw'

goto = requests.get('https://www.googleapis.com/youtube/v3/search?'+'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key,ch_id))
    
gotovid = json.loads(goto.text)
    
getvid = gotovid['items'][0]['id']['videoId']

def check_new_videos():
    
    try:
        
        with open('newvidjson.json','r') as js1:
            
            data = json.load(js1)
            
            print('Checking for New Videos..')
            
            if data['videoId']!=getvid:
                
                print('New video found')
                
                webbrowser.open('https://www.youtube.com/watch?v='+getvid)
                
            else:
                
                print('No New videos found')
    
    except FileNotFoundError:
        
        with open('newvidjson.json','w') as js1:
            
            data = {'videoId':getvid}
            
            json.dump(data,js1)
        
if __name__=='__main__':
    
    check_new_videos()
    
    
    


    


# In[ ]:




