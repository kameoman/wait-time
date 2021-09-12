import streamlit as st
import urllib3
from bs4 import BeautifulSoup
import requests

url = "http://usjinfo.com/attrWait.php?attr_id=2"

st.title('待ち時間アプリ')
http = urllib3.PoolManager()
response = http.request("GET",url)

if response.status == 200:
  print("正常通信")

data = BeautifulSoup(response.data, "lxml")
title = data.title.string
t_title = (title.split("|")[0])
print(t_title)
data.find_all("div", attrs={"class": "realtime_status"})
w_time = data.find_all("div", attrs={"class": "realtime_status"})[0].string
w_time_int = int(w_time.split("分")[0])
nowtime = data.find_all("h2")[1].string
n_time = (nowtime.split(">|<")[0])
print(n_time)
print(w_time_int)