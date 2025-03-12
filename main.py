# 功能：

#   提供 网页版界面，让用户输入 用户名、密码、日期、时间
#   调用 RHCC 订场逻辑
#   显示 订场结果
import streamlit as st
from rhcc_booking import login_and_book

st.title("RHCC 网球场自动订场")

username = st.text_input("用户名", "")
password = st.text_input("密码", "", type="password")
date = st.date_input("选择日期")
court_time = st.selectbox("选择时间", ["8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM"])  # 可扩展

if st.button("开始抢场"):
    result = login_and_book(username, password, date.strftime('%Y-%m-%d'), court_time)
    st.success(result)
