#-*-encoding:utf8-*-



import urllib2
import urllib
import re
import time
import random
import ssl
import json

#随机获取列表中的值，使用random中的random.choice()方法

#起点url 通过strip定位到|解析出|左边的中文和右边的简称

txt1_key = random.choice([k.decode("GBK") for k in open("k1.txt")])
txt1_name = txt1_key.split('|')[0]
txt1_jp = txt1_key.split('|')[1].encode("utf8")
qd = urllib.quote(txt1_jp).strip('%0A') 
print  "起点" + txt1_name +":"+ qd

#终点url 通过strip定位到|解析出|左边的中文和右边的简称
txt2_key = random.choice([k2.decode("GBK") for k2 in open("k2.txt")])
txt2_name = txt2_key.split('|')[0]
txt2_jp = txt2_key.split('|')[1].encode("utf8")
zd = urllib.quote(txt2_jp).strip('%0A')
print "终点" + txt2_name +  ":" + zd
    
##kw_bs = random.choice([k.decode("GBK") for k in open("k1.txt")]).encode("utf8")
##qd = urllib.quote(kw_bs).strip('%0A')  
##kw_ts = random.choice([k2.decode("GBK") for k2 in open("k2.txt")]).encode("utf8")
##zd = urllib.quote(kw_ts).strip('%0A')  


url = "http://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-04-09&from_station=" + qd +"&to_station=" + zd

context = ssl._create_unverified_context()

html = urllib2.urlopen(url,context=context).read()
html_page = json.loads(html)
print html
print html_page['messages']




##
##resp = json.loads(html)
##neirong = resp['data']['questionList']
##for i in neirong:
##    title = i['question']
##    a = "A" + i['ans1']
##    b = "B" + i['ans2']
##    c = "C" + i['ans3']
##    d = "D" + i['ans4']
##    wen = title + "\n" + a + "\n" + b + "\n" + c + "\n" + d + "\n"
##    f.writelines(wen)
##    f.writelines("\n")
