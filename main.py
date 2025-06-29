import requests
from dotenv import load_dotenv
import os

query = input("\n📰 What kind of news would you like to read today?: ")
print('\n')

# load variables from .env 
load_dotenv()
# get API key
key = os.getenv("NEWS_API_KEY")

# build API URL
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={key}"

print(url,"\n") # uncomment to view the generated API URL

# get data from the generated url
r = requests.get(url) 

#covert that data into python dictionary format using json()
data = r.json() 


'''
Now, data is a big dictionary that looks like:

{
  "status": "ok",
  "totalResults": 100,
  "articles": [ {article1}, {article2}, {article3}, ... ]
}
'''

# pull just the list of news articles from the dictionary.Now articles is a list of dictionaries. Each dictionary is one news article.
articles = data["articles"] 

# display each article
for index,article in enumerate(articles):
    print(f"{index+1}) Title : {article['title']}")
    print(f"   🔗 url : {article['url']}") 
    #to open the url - hold ctrl and click on the link and click open 
    print("\n--------------------------------------------------------------------------------------------------------------------------\n")

