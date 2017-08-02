from selenium import webdriver
import time

'''
/html/body/div[7]/div[1]/div/ul/li[1]/dl/dt/a   Titan
/html/body/div[7]/div[1]/div/ul/li[2]/dl/dt/a   
/html/body/div[7]/div[1]/div/ul/li[3]/dl/dt/a   
/html/body/div[7]/div[1]/div/ul/li[4]/dl/dt/a   
'''

def submit(n):
    hour = 21+n
    #td[3]表示星期三
    xpath = "/html/body/div[7]/div[2]/div[2]/table/tbody/tr/td[3]/div/div[" + str(hour) + "]/span"
    d.find_element_by_xpath(xpath).click()
    d.find_element_by_xpath("/html/body/div[7]/div[2]/div[3]/div/form/p[4]/input").click()
    time.sleep(1)
    d.find_element_by_xpath("/html/body/div[13]/form/p[1]/textarea").send_keys("liaozhenhua")
    d.find_element_by_xpath("/html/body/div[13]/form/p[2]/input").click()
    time.sleep(1)

def open_html():
#     d = webdriver.PhantomJS(executable_path="phantomjs.exe")
    d = webdriver.Firefox()
    
    d.get('http://wnlo-hust.ylab.cn/login.action')
    d.find_element_by_xpath("/html/body/div[1]/div/div/form/fieldset/p[1]/input").send_keys('xujuan')
    d.find_element_by_xpath("/html/body/div[1]/div/div/form/fieldset/p[2]/input").send_keys('ghb602826ghb')
    d.find_element_by_xpath("/html/body/div[1]/div/div/form/fieldset/p[3]/input").click()
    time.sleep(2)
    d.maximize_window()
    #
    d.find_element_by_xpath("/html/body/div[7]/div[1]/div/ul/li[1]/dl/dt/a").click()
    time.sleep(2)
    #
    d.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/p/a[4]").click()
    time.sleep(1)
    return d

#

def make_order():
    for i in range(4):
        try:
            submit(i)
        except:
            pass

if __name__ == "__main__":
    d = open_html()
    make_order()
    d.close()
    print("=====end=====")

