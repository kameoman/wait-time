import streamlit as st
import urllib3
from bs4 import BeautifulSoup
import requests
from PIL import Image

st.title('待ち時間アプリ')
if st.checkbox("ディズニーランド待ち時間"):
    if st.checkbox("ｽﾌﾟﾗｯｼｭ･ﾏｳﾝﾃﾝ待ち時間"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=112&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write (w_time)
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")


if st.checkbox("USJ関連情報"):
  url = "https://usjinfo.com/"
  http = urllib3.PoolManager()
  response = http.request("GET",url)
  data = BeautifulSoup(response.data, "lxml")
  w_time = data.find_all("div", attrs={"class": "business_hour"})
  w_time_str = str(w_time)
  open_time =w_time_str.split(">|<")[0]
  open_time1 =open_time.split("\n")[2]
  open_time2 =open_time.split("\n")[4]
  today = data.find_all("h2")[1]
  today = str(today)
  st.write(today[4:36])
  st.write("営業時間"+open_time1+"～"+open_time2)
  if st.checkbox("ジュラシックパーク待ち時間"):
    img = Image.open("usj-jurassic-park-the-ride-logo.png")
    img2 = Image.open("usj-jurassic-park-the-ride-long-necked-dinosaur-c.jpg")
    # img3 = Image.open("usj-jurassic-park-the-ride-logo.png")
    st.image(img)
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
    st.image(img2)

  if st.checkbox("NEW アメージング・アドベンチャー・オブ・スパイダーマン(TM)・ザ・ライド 4K3D"):
    img = Image.open("usj-the-amazing-adventures-of-spider-man-the-ride-logo.png")
    img2 = Image.open("usj-the-amazing-adventures-of-spider-man-the-ride-water-c.jpg")
    st.image(img)
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
    st.image(img2)

  if st.checkbox("ハリウッド・ドリーム・ザ・ライド"):
    img = Image.open("usj-hollywood-dream-the-ride-logo.png")
    img2 = Image.open("usj-hollywood-dream-the-ride-first-drop-c.jpg")
    st.image(img)
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
    st.image(img2)

  if st.checkbox("マリオカート ～クッパの挑戦状"):
    img = Image.open("usj-mario-the-ride-logo.png.png")
    img2 = Image.open("usj-mario-the-ride-ride.png")
    st.image(img)
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=28684"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    st.write("マリオカート ～クッパの挑戦状")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    # st.write(w_time_int)
    st.write(w_time_str+"分")
    st.image(img2)