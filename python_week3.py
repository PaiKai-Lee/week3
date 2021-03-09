import requests

import requests

url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
response=requests.get(url)
dataList=response.json()["result"]["results"]

with open("data.txt","w",encoding="utf-8") as file :
    for data in dataList:
        indexJpg=data["file"].lower().find(".jpg")
        print(data["stitle"],indexJpg)
        if indexJpg==-1:
            indexPng=data["file"].lower().find(".png")
            firstPng=data["file"][:indexPng]
            file.write(data["stitle"]+","+data["longitude"]+","+data["latitude"]+","+firstPng+".png"+"\n")
        else:
            firstJpg=data["file"][:indexJpg]
            file.write(data["stitle"]+","+data["longitude"]+","+data["latitude"]+","+firstJpg+".jpg"+"\n")


