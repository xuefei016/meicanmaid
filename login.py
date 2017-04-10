from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://meican.com/login")

bs_obj = BeautifulSoup(html, "html.parser")
username = bs_obj.find(id='email')
password = bs_obj.find(id='password')
sign_btn = bs_obj.find(id='signin')

username['value'] = "feixue8@creditease.cn"
password['value'] = "123456"

print(username)

html.close()



