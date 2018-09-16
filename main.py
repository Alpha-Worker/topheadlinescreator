from newsapi import NewsApiClient
import os
os.system("pip3 install newsapi-python")
# Init
newsapi = NewsApiClient(api_key='a2b7ec8bc6de4079b3e5951c964b940e')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en',country='us')

file = open("stuff.txt","r+")



for a in top_headlines['articles']:
    file.write(a['url']+'\n')
    file.write(a['title']+'\n\n')
    file.write(a['description']+"\n\n\n\n\n")
    


file.close()
