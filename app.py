# 빅공잼 유튜브
# https://www.youtube.com/watch?v=o25-om93D0E&t=1s&ab_channel=%EB%B9%85%EA%B3%B5%EC%9E%BC

import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설정
st.set_page_config(
    page_icon="🍙",
    page_title="미묘한 채널 스트림릿 배포하기",
    layout="wide"
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("미묘한 채널 페이지에 오신 것을 환영합니다. 👋")
st.subheader("스트림릿 기능 맛보기")

# 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
cols = st.columns((1, 1, 2))
cols[0].metric("3/19", "15 °C", "2")
cols[0].metric("3/20", "17 °C", "2 °F")
cols[0].metric("3/21", "15 °C", "2")
cols[1].metric("3/22", "17 °C", "2 °F")
cols[1].metric("3/23", "14 °C", "-3 °F")
cols[1].metric("3/24", "13 °C", "-1 °F")

# 라인 그래프 데이터 생성(with, Pandas)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
columns=['a', 'b', 'c'])

# 컬럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)