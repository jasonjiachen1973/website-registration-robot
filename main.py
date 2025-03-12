# 功能：

#   提供 网页版界面，让用户输入 用户名、密码、日期、时间
#   调用 RHCC 订场逻辑
#   显示 订场结果
import streamlit as st
from rhcc_booking import login_and_book

# Streamlit 界面
st.title("RHCC 网球场自动订场")

username = st.text_input("用户名", "")
password = st.text_input("密码", "", type="password")
date = st.date_input("选择日期")

# 选择网球场地
court_options = ["Tennis Court 1", "Tennis Court 2", "Tennis Court 19", "Tennis Court 20"]
selected_court = st.selectbox("选择场地", court_options)

# 选择时间（6:30 AM - 8:30 PM，每小时一个时段）
time_options = [f"{h}:30 AM" for h in range(6, 12)] + ["12:30 PM"] + [f"{h}:30 PM" for h in range(1, 9)]
selected_time = st.selectbox("选择时间", time_options)

if st.button("开始抢场"):
    result = login_and_book(username, password, date.strftime('%Y-%m-%d'), selected_court, selected_time)
    st.success(result)

