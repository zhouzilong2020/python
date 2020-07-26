from selenium import webdriver
from selenium.webdriver import ChromeOptions
import threading
import time

options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
#options.add_argument('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
options.add_argument(''''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Host: passport.zhihuishu.com
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36''')
path = "https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin#signin"
url = "https://onlineh5.zhihuishu.com/onlineWeb.html#/studentIndex"
browser = webdriver.Chrome(options = options)
browser.get(url)

def login(id, pwd):
    id_input = browser.find_element_by_id('lUsername')
    pwd_input = browser.find_element_by_id('lPassword')
    login_btn=browser.find_element_by_class_name('wall-sub-btn')
    
    id_input.send_keys(id)
    pwd_input.send_keys(pwd)
    time.sleep(1)
    login_btn.click()
    time.sleep(10)

def to_course(course_name):
    current = browser.current_window_handle
    course_link = browser.find_element_by_partial_link_text(course_name)
    course_link.click()

    time.sleep(5)
    # 当前打开了两个窗口，现在切换到新的窗口去
    handles=browser.window_handles
    for handle in handles:
        if handle!=current:
            browser.switch_to.window(handle)

    time.sleep(10)
    try:
        video = browser.find_element_by_id('mediaplayer')
        video.click()
    except:
        pass

def is_exist():
    while True:
        try:
            browser.switch_to.default_content()
            box = browser.find_element_by_class_name("topic-option")
            box[0].click()
            browser.switch_to.default_content()
            browser.find_element_by_link_text("关闭").click()
        except:
             browser.switch_to.parent_frame()
        time.sleep(5)

def is_end():
    while True:
        try:
            video = browser.find_element_by_id('mediaplayer')#定位视频窗口
            current_time = video.find_element_by_class_name('currentTime').get_attribute('textContent')  
            total_time = video.find_element_by_class_name('duration').get_attribute('textContent')
            print(current_time, total_time)
            if current_time==total_time:
                js="document.ElementById('nextBtn').click()"#js脚本
                browser.execute_script(js)
            time.sleep(10)#10秒检测一次
        except:
            current_time='00:00'
            total_time='00:01'

if __name__=='__main__':
    id = '18817815176'
    pwd = 'ZHOUzilong1003'
    course_name = '音乐艺术概论'

    login(id, pwd)
    to_course(course_name)

    t1 = threading.Thread(targety = is_exist)
    t2 = threading.Thread(targety = is_end)
    t2.start()
    time.sleep()
    t1.start()
