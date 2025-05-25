import yfinance as yf
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("📈 AAPL Candlestick Chart - Daily Data")

# Get 1 month daily data
df = yf.download("AAPL", period="1mo", interval="1d")

st.write("Raw Data:", df.head())
st.write("Columns:", df.columns)

if df.empty:
    st.error("No data received from yfinance!")
else:
    df = df.reset_index()  # Make 'Date' a column
    
    # Convert Date to datetime if needed
    if df['Date'].dtype == 'object':
        df['Date'] = pd.to_datetime(df['Date'])
    
    st.write("Date dtype:", df['Date'].dtype)

    st.write(df.head())        # Show top rows
    st.write(df.dtypes)        # Show datatypes


    fig = go.Figure(data=[go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])

    st.plotly_chart(fig, use_container_width=True)
