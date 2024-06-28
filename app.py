import streamlit as st
import requests

st.title('Server Communication Test')

# 요청을 보낼 URL
url = 'https://httpbin.org/get'

# HTTP GET 요청 보내기
response = requests.get(url)

# 응답 상태 코드와 내용을 스트림릿 애플리케이션에 표시
st.write('Response Status Code:', response.status_code)
st.write('Response Content:', response.json())
