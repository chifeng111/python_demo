# coding: utf-8
import re 
import requests
from bs4 import BeautifulSoup
from scipy.stats._continuous_distns import chi



def demo2():
    with open("test.txt", 'r') as f:
        html = f.read()
#     print(html)
    reg = r'href="(.*?)"'
    url = re.findall(reg, html)
    print(url)
    for i in url:
        print(i)

def demo1():
    r = requests.get("http://www.baidu.com")
    print(r)
    r.encoding = r.apparent_encoding
    print(r.apparent_encoding)
    print(r.text)

if __name__ == '__main__':
#     demo1()
#     demo2()
    with open("test.txt", 'r') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    b = soup.body
#     print(b.name,b.string, b.attrs)
    print(b.children)#是一个iterator
    a = soup.a
    print(a.get_string)
    for child in b.children:
#         print("%()----->%()".format(child.attrs[href], child.string))
        try:
            print("{}----->{}".format(child.attrs['href'], child.get_string))
        except:
            pass






    