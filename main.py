import streamlit as st
import urllib3
from bs4 import BeautifulSoup
import requests
from PIL import Image

st.title('待ち時間アプリ')
left_column,center_column,right_column = st.columns(3)
button1 = left_column.checkbox("TDL")
button2 = center_column.checkbox("TDS")
button3 = right_column.checkbox("USJ")

if button1:
    if st.checkbox("ｽﾌﾟﾗｯｼｭ･ﾏｳﾝﾃﾝ待ち時間"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=112&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write(w_time)
        # checkbox1 = st.checkbox("お問い合わせ")
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")

    if st.checkbox("ﾋﾞｯｸﾞｻﾝﾀﾞｰ･ﾏｳﾝﾃﾝ"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=110&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write(w_time)
        # expander1 = st.expander("お問い合わせ")
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")

    if st.checkbox("ﾐｯｷｰの家とﾐｰﾄ･ﾐｯｷｰ"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=126&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write(w_time)
        # expander1 = st.expander("お問い合わせ")
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")
        
    if st.checkbox("ﾋﾟｰﾀｰﾊﾟﾝ空の旅"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=114&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write(w_time)
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")

      st.checkbox("ﾌﾟｰさんのﾊﾆｰﾊﾝﾄ")
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=123&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write(w_time)
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")

    if st.checkbox("ﾊﾞｽﾞ･ﾗｲﾄｲﾔｰのｱｽﾄﾛﾌﾞﾗｽﾀｰ"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=134&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write(w_time)
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")

    if st.checkbox("ｽﾍﾟｰｽ･ﾏｳﾝﾃﾝ"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=133&park=land"
      http = urllib3.PoolManager()
      response = http.request("GET",url)
      data = BeautifulSoup(response.data, "lxml")
      data.find_all("div", attrs={"class": "info-data-value"})
      w_time = data.find_all("div", attrs={"class": "info-data-value"})[0].string
      if w_time ==  '\n\t\t\t\t\t\t\t受付終了\n\t\t\t\t\t':
        st.write(w_time)
      else:
        w_time_int = int(w_time.split("分")[0])
        w_time_str = str(w_time_int)
        n_time = data.find_all("span", attrs={"class": "small"})[0].string
        n_time1 = n_time[1:6]
        st.write(n_time1+"時点")
        st.write(w_time_str+"分")

if button2:
    if st.checkbox("ｿｱﾘﾝ：ﾌｧﾝﾀｽﾃｨｯｸ･ﾌﾗｲﾄ待ち時間"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=405&park=sea"
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
    if st.checkbox("ﾄｲ･ｽﾄｰﾘｰ･ﾏﾆｱ！の待ち時間"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=173&park=sea"
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
    if st.checkbox("ﾄｲ･ｽﾄｰﾘｰ･ﾏﾆｱ！の待ち時間"):
      url = "https://tokyodisneyresort.info/attrWait.php?attr_id=173&park=sea"
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


if button3:
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
  if st.checkbox("ザ・フライング・ダイナソー"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=58"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")
  if st.checkbox("ミニオン・ハチャメチャ・ライド"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=71"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")
  if st.checkbox("ハリーポッター・アンド・ザ・フォービドゥン・ジャーニー™"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=30"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")
  if st.checkbox("ヨッシー・アドベンチャー"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=28685"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")
  if st.checkbox("ジョーズ(R)"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=1"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")
  if st.checkbox("フライト・オブ・ザ・ヒッポグリフ™"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=29"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")
  if st.checkbox("エルモのゴーゴー・スケートボード"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=44"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")
  if st.checkbox("モッピーのバルーン・トリップ"):
    url = "https://usjinfo.com/wait/sp/attrWait.php?attr_id=45"
    http = urllib3.PoolManager()
    response = http.request("GET",url)
    data = BeautifulSoup(response.data, "lxml")
    data.find_all("div", attrs={"class": "realtime_status"})
    w_time = w_time = data.find_all("div", attrs={"data-role": "button"})[0].string
    w_time_int = int(w_time.split("分")[0])
    w_time_str = str(w_time_int)
    nowtime = data.find_all("li", attrs={"data-role": "list-divider"})[0].string
    n_time = (nowtime.split(">|<")[0])
    st.write(n_time)
    st.write(w_time_str+"分")