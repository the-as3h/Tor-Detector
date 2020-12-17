#This code stops executing when it found the tor node in csv file those ip addresses after that will not check for Detection
#if you want to check the whole csv file. Then just remove specified commented lines. comment1,comment2,comment3,comment4,comment5 and comment6

import pandas as pd
import requests
data=pd.read_csv(r"/root/mycs.csv")
s=data["Source"]
tor=requests.get("https://www.dan.me.uk/torlist/")
tor1=str(tor.text)
iplists=tor1.split('\n')
for index,value in s.items():
    a=False                                           #comment 1
    for i in iplist:
        if value==i:
           a=True                                     #comment 2
           print("This is the tor node" +value)
           break
    if a==True:                                       #comment 3
       break                                          #comment 4
    else:                                             #comment 5
       continue                                       #comment 6



"""
If you want to check a single ip address just replace the above for loop code with this.


ip='1.2.3.4' #ip which i want to check
for i in iplist:
    if i==ip:
       print("This is a tor node" +value)
       break



"""
