import requests
import time
from requests import session
from lxml import html
from pync import Notifier
import os

# Notifier.notify("New messages for you", group=os.getpid())

payload = {
    'action': 'login',
    'username': 'f2015533',
    'password': '^Bitslife$005'
}

# with session() as c:
# 	c.post('https://10.1.0.10:8090',data=payload)
# 	response = c.get('https://10.1.0.10:8090')
# 	tree = html.fromstring(response.content)
# 	print(response.headers)
# 	print(response.text)
# os.system("notify-send 'Sebastin' 'There is a message for you'")

with session() as c:
    c.post('http://10.1.1.242/moodle/login/index.php', data=payload)
    response = c.get('http://10.1.1.242/moodle/my/')
    tree = html.fromstring(response.content)
    buyers = tree.xpath('//div[@class="activity_info"]/ancestor::div[1]/div[@class="course_title"]/h2/a/text()')
    stra=""
    for i in buyers:
    	stra = stra + i + "\n"
    stra = "You have forum posts from\n" + stra
    # print(stra)
    Notifier.notify(stra, title="Message from moodle")
   	



    # print(response.headers)
    # print(response.text)

# '//div[@class="activity_info"]/div/div/div/div[@class="collapsibleregioncaption"]/text()'
# tree = html.fromstring(response.content)
# sid062956
# '//div[@class="buyer-name"]/text()'

# f2015327
# goodgodChinm@y1