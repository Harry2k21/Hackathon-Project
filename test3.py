import requests
import json

def coke_url():
    
    url = f'https://esgapiservice.com/api/authorization/search?q=the%20coca-cola&token=66b0034b9254f3338c356fc3461bc661'
    url = f'https://esgapiservice.com/api/authorization/search?q=pepsi%20&token=66b0034b9254f3338c356fc3461bc661'

    response = requests.get(url)
    data = response.json()
    name1 = data
    nutrition1 = data[0]["environment_grade"]
    #print(name1)
    print(nutrition1)
coke_url()