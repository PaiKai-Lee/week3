import requests

import requests

url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
response=requests.get(url)
dataList=response.json()["result"]["results"]        #抓取results內的資料

with open("data.txt","w",encoding="utf-8") as file :
    for data in dataList:
        dataFile=data["file"]                        #抓取key="file"內的資料(圖片連結網址)
        fileList=dataFile.split("http://")           #將整串字串以列表方式分開
        firstImg=fileList[1]                         #取的第一張圖片的連結
        print(firstImg)
        file.write(data["stitle"]+","+data["longitude"]+","+data["latitude"]+","+"http://"+firstImg+"\n")


