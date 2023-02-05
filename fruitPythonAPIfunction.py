import requests
import json

def scrape_all_fruits():
    
    url = f'https://fruityvice.com/api/fruit/banana'
    response = requests.get(url)
    data = response.json()
    name1 = data["name"]
    nutrition1 = data["nutritions"]
    print(name1, "\n" ,nutrition1)

print(scrape_all_fruits())