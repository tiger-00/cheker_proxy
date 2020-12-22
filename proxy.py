import random
import requests
import threading
from time import sleep


print("Developer :mounir AL bdullha 👨🏻‍💻")
print("snapchat:ar5824")
fill = input("put file proxy:")
def pro():
    try:
        proxy = open(fill, 'r').read().splitlines()
        proxylist = []
        for prox in proxy:
            proxylist.append(prox)
        randomproxy = str(random.choice(proxylist))
        RP = {
         'https': randomproxy,
         'http': randomproxy
        }
        url = 'https://www.google.com/'
        r = requests.get(url, proxies=RP).text
        print(randomproxy)
        with open("good_proxy.txt", 'a') as lo:
            lo.write(randomproxy + '\n')
    except requests.exceptions.ConnectionError:
        pass
theards = []
for i in range(1500):
    th1 = threading.Thread(target=pro)
    th1.start()
    theards.append(th1)
for th2 in theards:
    th2.join()