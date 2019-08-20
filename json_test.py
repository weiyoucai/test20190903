import json


#json转python
jsonStr='{"hobby":["basketball","football","music"],"breakfast":["egg","milk","rice"]}'

jsonData=json.loads(jsonStr)

print(jsonData)
print(type(jsonData))
print(jsonData["breakfast"])

#python转json

jsonData2={"hobby":["basketball","football","music"],"breakfast":["egg","milk","rice"]}

jsonStr2=json.dumps(jsonData2)

print(jsonStr2)
print(type(jsonStr2))


#读取本地json

#path1=r""
#with open(path1,"rb") as f:
 #   Data1=json.load(f)
 #   print(Data1)
  #  print(type(Data1))   #python智能地把json数据转换成字典


#写json到本地

path2=r"D:\01学习\000人工智能\VikJSON\1.json"
jsonData3={"hobby":["basketball","football","music"],"breakfast":["egg","milk","rice"]}
with open(path2,"w") as f:
    jsonStr3=json.dump(jsonData3,f)

