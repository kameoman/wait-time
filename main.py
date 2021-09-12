import streamlit as st
import urllib3
from bs4 import BeautifulSoup
import requests

st.title('待ち時間アプリ')
if st.checkbox("ジュラシックパーク待ち時間"):
  url = "http://usjinfo.com/attrWait.php?attr_id=2"
  http = urllib3.PoolManager()
  response = http.request("GET",url)
  data = BeautifulSoup(response.data, "lxml")
  title = data.title.string
  t_title = (title.split("|")[0])
  st.write(t_title)
  data.find_all("div", attrs={"class": "realtime_status"})
  w_time = data.find_all("div", attrs={"class": "realtime_status"})[0].string
  w_time_int = int(w_time.split("分")[0])
  w_time_str = str(w_time_int)
  nowtime = data.find_all("h2")[1].string
  n_time = (nowtime.split(">|<")[0])
  st.write(n_time)
  # st.write(w_time_int)
  st.write(w_time_str+"分")

if st.checkbox("NEW アメージング・アドベンチャー・オブ・スパイダーマン(TM)・ザ・ライド 4K3D"):
  url = "http://usjinfo.com/attrWait.php?attr_id=18"
  http = urllib3.PoolManager()
  response = http.request("GET",url)
  data = BeautifulSoup(response.data, "lxml")
  title = data.title.string
  t_title = (title.split("|")[0])
  st.write(t_title)
  data.find_all("div", attrs={"class": "realtime_status"})
  w_time = data.find_all("div", attrs={"class": "realtime_status"})[0].string
  w_time_int = int(w_time.split("分")[0])
  w_time_str = str(w_time_int)
  nowtime = data.find_all("h2")[1].string
  n_time = (nowtime.split(">|<")[0])
  st.write(n_time)
  # st.write(w_time_int)
  st.write(w_time_str+"分")

if st.checkbox("ハリウッド・ドリーム・ザ・ライド"):
  url = "http://usjinfo.com/attrWait.php?attr_id=8"
  http = urllib3.PoolManager()
  response = http.request("GET",url)
  data = BeautifulSoup(response.data, "lxml")
  title = data.title.string
  t_title = (title.split("|")[0])
  st.write(t_title)
  data.find_all("div", attrs={"class": "realtime_status"})
  w_time = data.find_all("div", attrs={"class": "realtime_status"})[0].string
  w_time_int = int(w_time.split("分")[0])
  w_time_str = str(w_time_int)
  nowtime = data.find_all("h2")[1].string
  n_time = (nowtime.split(">|<")[0])
  st.write(n_time)
  # st.write(w_time_int)
  st.write(w_time_str+"分")