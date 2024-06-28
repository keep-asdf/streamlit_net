import streamlit as st
import requests

# st.title('Server Communication Test')

# # 요청을 보낼 URL
# url = 'https://httpbin.org/get'

# # HTTP GET 요청 보내기
# response = requests.get(url)

# # 응답 상태 코드와 내용을 스트림릿 애플리케이션에 표시
# st.write('Response Status Code:', response.status_code)
# st.write('Response Content:', response.json())

import streamlit as st

# 페이지 제목
st.title('My Streamlit App')

# 간단한 출력
st.write('Hello, Streamlit!')

# 데이터 처리
data = [1, 2, 3, 4, 5]
squared_data = [x**2 for x in data]
st.write('Original data:', data)
st.write('Squared data:', squared_data)

# 차트 시각화
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(data, squared_data)
st.pyplot(fig)

# print 문 (서버 콘솔에 출력됨)
print('This is printed in the server console')
