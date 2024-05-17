import streamlit as st 
import pandas as pd
import helper

st.title('financial extraction tool')
financial_data_df = pd.DataFrame({
    "Measure":["Comapny Name","Stock Symbol","Revenue","Net Income","EPS"],
    "Value":["","","","",""]
})

col1,col2 = st.columns([3,2])

with col1 :
    st.header('data extraction tool')
    news_article = st.text_area("paste your article here",height=300)
    if st.button('extract'):
        financial_data_df = helper.extract_info(news_article)
        
with col2:
    st.markdown("<br/>" * 3 ,unsafe_allow_html=True)
    st.dataframe(
        financial_data_df,
        column_config = {
            "Measure " : st.column_config.Column(width=150),
            "Value " :st.column_config.Column(width=150)
        },
        hide_index=True
    )