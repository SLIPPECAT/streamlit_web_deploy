import streamlit as st
import FinanceDataReader as fdr
import datetime

# Finacne Data Reader
# https://github.com/financedata-org/FinanceDataReader
# pip install finance-datareader

date = st.date_input(
    '조회 시작일을 선택해 주세요.',
    datetime.datetime(2024, 1, 1)
)

code = st.text_input(
    '종목코드',
    value='',
    placeholder='종목코드를 입력해 주세요.'
)

if code and date:
    df = fdr.DataReader(code, date)
    # 날짜 기준으로 정렬
    # 종가 기준으로 가져오기
    data = df.sort_index(ascending=True).loc[:, 'Close']
    st.line_chart(data)

st.write('spc삼립 주식코드: 005610')