import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="Investment Dashboard",layout="wide")
portfolio=pd.read_csv("portfolio.csv")
mf=pd.read_csv("mutual_funds.csv")
prices=[]
for t in portfolio["Ticker"]:
    try:
        prices.append(yf.Ticker(t).fast_info["lastPrice"])
    except:
        prices.append(None)
portfolio["CurrentPrice"]=prices
portfolio["Invested"]=portfolio.Qty*portfolio.BuyPrice
portfolio["CurrentValue"]=portfolio.Qty*portfolio.CurrentPrice
st.title("Portfolio Dashboard")
st.dataframe(portfolio)
fig=px.pie(portfolio,values='CurrentValue',names='Stock')
st.plotly_chart(fig,use_container_width=True)
st.subheader('Mutual Funds')
st.dataframe(mf)
