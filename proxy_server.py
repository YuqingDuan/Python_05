#爬虫防屏蔽手段之代理服务器
#代理服务器：所谓代理服务器，是一个处于我们与互联网中间的服务器。如果使用代理服务器，我们浏览信息的时候，先向代理服务器发出Req，然后由代理服务器想互联网获取信息，再返回给我们。
#使用代理服务器进行网站信息爬取，可以很好的解决IP限制问题
#网上有一些提供免费代理服务器的站点，如：西刺免费代理ip...
#代理ip实时有效！
#实际工作中使用代理ip池，list实现

import urllib.request

#自定义使用代理服务器的函数use_proxy(url, proxy_ip)，其中url是要爬取的目标网站，proxy_ip是我们使用的代理服务器ip
def use_proxy(url, proxy_ip):
    #构造代理对象proxy
    proxy=urllib.request.ProxyHandler({"http" : proxy_ip})
    #将proxy封装到opener对象之内
    opener=urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    #将opener设置全局化
    urllib.request.install_opener(opener)
    #爬取网站
    data=urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    #将结果返回
    return data

url="http://www.baidu.com"
proxy_ip="114.243.254.248:8888"
data=use_proxy(url, proxy_ip)
print(len(data))
