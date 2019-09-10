#encoding:utf-8
#python2
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def getHtml(url):
    page = requests.get(url)
    html = page.text
    return html

r = requests.get("http://www.fayangao.cn/fayanjianghuagao/shengzhang/3.html")
with open("douban.py","wb") as f:
    f.write(r.text)
#print r.text
with open("douban.py","r") as t:
    s = t.read()
tt = '尊敬的' + '[\s\S]*?' + '(转载请保留)'
pattern = re.compile(tt)
dd = ''.join(pattern.findall(s))
dd = dd.replace('(转载请保留)','')
#findall返回列表
dd = dd.decode('utf-8')
with open("douban.py","wb") as x:
    x.write(dd)
