import json
import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/locations/+50.8741+004.3371/nearbyCities"

querystring = {"radius":"100","countryIds":"BE"}
## radius is limited to 100 due to the free RapidAPI plan but it seems to work ;)
headers = {
    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
    'x-rapidapi-key': "3b4eed5ad2msh6f39fa82d4ccf3cp1c7041jsn917b8d17b90f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
json_list = json.loads(response.text)

for item in json_list['data']:
   display_name = item['city']
   print(display_name)