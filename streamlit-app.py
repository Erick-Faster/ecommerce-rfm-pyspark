import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(
    page_title="RFM Analysis",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://erick-faster.github.io/portfolio/',
        'Report a bug': "https://www.linkedin.com/in/erickfasterra/",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

@st.cache
def rfm_data():
    df = pd.read_csv('data/refined/output_customer.csv', encoding='utf-8')
    return df

df = rfm_data()

st.title("RFM Analysis (by Erick Faster")
st.write(df)

