
import pandas as pd
import yfinance as yf
import streamlit as st

import streamlit as st
import pandas as pd
import numpy as np

st.title('Stock Market App')
st.write("This is my hope to hike")
ticker_symbol = st.text_input('Enter the stock ticker symbol', 'AAPL')
ticker_data = yf.Ticker(ticker_symbol)


starting_date=st.date_input('Enter the starting date',value=pd.to_datetime('2022-05-31'))
ending_date=st.date_input('Enter the ending date',value=pd.to_datetime('2022-07-30'))
#ticker_data = yf.Ticker('AAPL')
#st.write('I am going to show you the data of Apple Inc.')
#st.write(ticker_data)
hist=ticker_data.history(start=starting_date,end=ending_date)
#st.write('I am going to show you the historical data of Apple Inc.')
#st.write(hist)  small data frame
st.dataframe(hist ) # big data frame with scroll bar

#st.write('This plot is volume of stock')
#st.line_chart(hist.Volume)
#st.write('This plot is for price of stock')
#st.line_chart(hist.Close)

col1,col2=st.columns(2)
with col1:
    st.write('This plot is volume of stock')
    st.line_chart(hist.Volume)
with col2:
    st.write('This plot is for price of stock')
    st.line_chart(hist.Close)