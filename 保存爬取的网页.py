import urllib.request


response=urllib.request.urlopen("https://www.sina.com.cn/")
data=response.read()
#print(data)
print(type(data))
print(len(data))
print(response.getcode())
print(response.geturl())
url2='https://www.so.com/s?ie=utf-8&src=hao_360so_b&shb=1&hsid=231871b002576062&q=%E6%88%91%E8%A6%81%E8%87%AA%E5%AD%A6'
url3='https://www.so.com/s?ie=utf-8&src=hao_360so_b&shb=1&hsid=231871b002576062&q=我要自学'

print(urllib.request.unquote(url2))
#with open(r"D:\BaiduNetdiskDownload\2.html","wb") as f:
 #   f.write(data)

urllib.request.urlretrieve(url2,filename=r"D:\BaiduNetdiskDownload\3.html")
urllib.request.urlcleanup()

#反 反爬虫 模拟浏览器设置
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"}
req=urllib.request.Request(url,headers=headers)
response2=urllib.request.urlopen("url2")
