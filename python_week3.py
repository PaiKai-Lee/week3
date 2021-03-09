import requests

import requests

url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
response=requests.get(url)
dataList=response.json()["result"]["results"]

with open("data.txt","w",encoding="utf-8") as file :
    for data in dataList:
        dataFile=data["file"]
        fileList=dataFile.split("http://")
        firstImg=fileList[1]
        print(firstImg)
        file.write(data["stitle"]+","+data["longitude"]+","+data["latitude"]+","+"http://"+firstImg+"\n")


