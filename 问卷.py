import requests

url = r'https://tongjistudent.wjx.cn/user/qlist.aspx?u=%e6%89%8b%e6%9c%ba%e7%94%a8%e6%88%b7g0xtoyb1buuqdrqsc9egsw&userSystem=1&systemId=55926111'
data = {'register-user-name':'1851201', 
        'register-user-password': 'ZHOUzilong1003'' 
    }
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Referer": url,
           "X-Requested-With": "XMLHttpRequest"
        }

session = requests.session()
loginpage = session.post(url, data=data)

url_login = r'https://tongjistudent.wjx.cn/user/newqlist.aspx?u=手机用户g0xtoyb1buuqdrqsc9egsw&userSystem=1&systemId=55926111'
item = 


1+1
2+2