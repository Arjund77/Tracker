import requests
import json
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/realme-xt-pearl-blue-64-gb/p/itm731360fdbd273?pid=MOBFJYBE25FEJZJN&srno=b_1_6&otracker=nmenu_sub_Electronics_0_Realme&lid=LSTMOBFJYBE25FEJZJN432EHB&fm=organic&iid=bb4e1aa0-9869-48a4-aaea-bf76685d1d54.MOBFJYBE25FEJZJN.SEARCH&ppt=browse&ppn=browse&ssid=hwu5bjps9c0000001574960665400"
r =requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
x=soup.find_all('div', class_ ='_1vC4OE _3qQ9m1')
'''print(soup.prettify())'''
print(x)
print(x[0].text)