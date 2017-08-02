from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

'''
/html/body/div[7]/div[1]/div/ul/li[1]/dl/dt/a   Titan
/html/body/div[7]/div[1]/div/ul/li[2]/dl/dt/a   透射电镜
/html/body/div[7]/div[1]/div/ul/li[3]/dl/dt/a   场发射扫描电镜
/html/body/div[7]/div[1]/div/ul/li[4]/dl/dt/a   双束电镜
'''

def submit(n):
    hour = 21+n
    #td[3]表示星期三
    xpath = "/html/body/div[7]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[" + str(hour) + "]/span"
    d.find_element_by_xpath(xpath).click()
    d.find_element_by_xpath("/html/body/div[7]/div[2]/div[3]/div/form/p[4]/input").click()
    time.sleep(1)
    d.find_element_by_xpath("/html/body/div[13]/form/p[1]/textarea").send_keys("liaozhenhua")
    d.find_element_by_xpath("/html/body/div[13]/form/p[2]/input").click()
    time.sleep(1)

d = webdriver.PhantomJS(executable_path="phantomjs.exe")
# d = webdriver.Firefox()

d.get('http://wnlo-hust.ylab.cn/login.action')
time.sleep(1)
d.find_element_by_id("userName").send_keys('liaozhenhua')
d.find_element_by_id("password").send_keys('123456')
d.find_element_by_id("loginBtn").click()
time.sleep(2)
d.maximize_window()
#选择设备
d.find_element_by_xpath("/html/body/div[7]/div[1]/div/ul/li[2]/dl/dt/a").click()
time.sleep(2)
#切换到下周
d.find_element_by_xpath("/html/body/div[7]/div[2]/div[1]/p/a[4]").click()
time.sleep(1)
d.get_screenshot_as_file("1.jpg")

#预约
for i in range(8):
    try:
        submit(i)
    except:
        d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        d.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        # ActionChains(d).move_by_offset(10, 10).perform()
        time.sleep(0.5)

d.close()

'''
/html/body/div[7]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[21]/span
'''

