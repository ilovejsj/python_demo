# -*- coding: utf-8 -*-

'''
最简单的爬虫代码 不用构造任何东西
import urllib2

linkopen = urllib2.urlopen("http://www.baidu.com")
print linkopen.read()


'''


这里是模拟登录CSDN，其中的代码全部是以【python 模拟登录 CSDN】【python CSDN 登录】等搜索而来，可能百度搜不到准确的答案。
'''
构造Requset

import urllib
import urllib2


#参考http://cuiqingcai.com/947.html中的代码，但是网站在该代码发布N久时间以后结果调整，登录的时候要带上lt、execution两个参数，
#至于怎么找到lt、execution，就登录页面源码中找。或者百度一下【CSDN lt】或者【CSDN execution】看下别人是怎么说的。
values = {}
values['username'] = "帐号"
values['password'] = "密码"
values['lt'] = "同样要传递的参数"
values['execution'] = "同样要传递的参数"
values['_eventId'] = "submit"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
'''


'''
也是搜的，当时只是直接想着拿来用，没想过为什么这些代码能实现。
'''

import requests
from bs4 import BeautifulSoup
 
url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
 
sess = requests.session()#群里问了一下说是【保存持久会话】
 
html1 = sess.get(url).text #效果等同于urlopen(xxx).read(),返回上面url里的内容
 
soup1 = BeautifulSoup(html1)#用bs4方法，没了解过，就理解成构建页面。
 
p1 = soup1.select("[name=lt]")[0]["value"] #这里找lt的值
p2 = soup1.select("[name=execution]")[0]["value"] #这里找execution的值
 
data = {
        "lt": p1,
        "execution": p2,
        "_eventId": "submit",
        "username": "帐号",
        "password": "密码"
        }
 
r = sess.post(url, data)  使用post的方法
 
msg = BeautifulSoup(sess.get('http://msg.csdn.net/').text)
print msg
