#图片爬虫：所谓图片爬虫，就是从互联网中自动的把对方服务器上的图片爬下来的爬虫程序。
#淘宝图片爬虫实战
#不用抓包版

import urllib.request
import re

#设置在淘宝要搜索的关键字
keyword="短裙"
#关键字中文编码处理
keyword=urllib.request.quote(keyword)
#对爬虫进行浏览器伪装处理
headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0")
#创建opener对象, 并把header头添加进去
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#将opener对象全局化
urllib.request.install_opener(opener)

#双重for循环遍历得到每张图片(外层循环遍历页数，内层循环遍历每一页的图片)
for i in range(0, 101):
    #每一页的url
    #https://s.taobao.com/search?q=%E7%9F%AD%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20181105&ie=utf8&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0
    #https://s.taobao.com/search?q=%E7%9F%AD%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20181105&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
    #https://s.taobao.com/search?q=%E7%9F%AD%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20181105&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88
    url="https://s.taobao.com/search?q="+ keyword + "&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20181105&ie=utf8&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&" + str(i*44)
    #获取每一页的数据
    data=urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    #查看网页源码找到图片路径
    #"pic_url":"//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i1/129496241/TB2lZqrzgaTBuNjSszfXXXgfpXa_!!0-saturn_solar.jpg"
    regex='"pic_url":"//(.*?)"'
    imageList=re.compile(regex).findall(data)
    for j in range(0, len(imageList)):
        this_image=imageList[j]
        this_image_url="http://" + this_image
        #存放到本地
        file="A:/img/" + str(i) + str(j) + ".jpg"
        urllib.request.urlretrieve(this_image_url, filename=file)
    















