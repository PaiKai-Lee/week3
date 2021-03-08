import requests


url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
response=requests.get(url)
dataList=response.json()["result"]["results"]
print(dataList)