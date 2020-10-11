import requests
import config
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Indian",
    "location": "Melbourne"
}
res = requests.get(url, headers=headers, params=params)
businesses = res.json()["businesses"]
businesses = [business["name"]
              for business in businesses if business["rating"] > 4.5]
# print(businesses)
for business in businesses:
    print(business)
