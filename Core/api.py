import requests
import json

#Good resource: "https://www.dataquest.io/blog/python-api-tutorial/"


po = {"name": "name1", "parents":[{
    "name": "name2", "age": 61},
    {"name": "name3", "age": 61 }]}

#every python object could be converted to json with json.dumps(obj). Could be also added indent atribute, with whom is printed object clearer
print(json.dumps(po, indent=4))

#python GET request without params
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.json()) #return dict, no need to convert to python dict with json.loads()
position = response.json()['iss_position']
longitude = position['longitude']
latitude = position['latitude']
print(f'Position of ISS in the moment: Latitude: {latitude} , Longitude: {longitude}')

#python GET request with params. HINT - you should always use API documentation. If documentation is well written, you will
#always know how to perform every request to specified REST API

#you should give parameters to get method with optianal keyword argument params like dictionary object. Second way is to directly
#put parameters in URL.

url = "https://api.agify.io/"
resp = requests.get(url, params={"name": "Dusan"})
print(resp.json())
age = resp.json()['age']
print(f'Based on statistic, guy with name "Dusan" is average {age} years old!')

