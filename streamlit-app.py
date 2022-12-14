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

labels = {
    'CustomerClass': 'Customer Class',
    'Count': 'Customer Count',
    '%': 'Percentage of Total Customers',
    'MeanRecency':'Average Recency',
    'MeanFrequency':'Average Frequency',
    'MeanMonetary': 'Average Monetary',}

category_orders = {
    'CustomerClass': ['Champion', 'Loyal', 'Potential Loyalist', 'Promising', 'New Customer', 'Need Attention', 'Cannot Lose Them', 'About To Sleep', 'At Risk', 'Hibernating', 'Lost'] 
}

color_sequence = ["#11B940", "#45C569", "#79D191", "#79D191", "#E1E8E1", "#E2DBD3", "#E3CEC5", "#E5B4A9","#E97F71", "#ED4A39", "#F01500"]

st.title("RFM Analysis (by Erick Faster)")

fig1 = px.bar(df, x="Count", y="CustomerClass", orientation='h', color='CustomerClass',
              color_discrete_sequence=color_sequence,
              category_orders = category_orders,
              labels=labels)
fig1.update_layout(title='Number of Customers by Class', showlegend=False)

fig2 = px.scatter(df, x="MeanRecency", y="MeanMonetary", color="CustomerClass",
                 size='Count', color_discrete_sequence=color_sequence, category_orders = category_orders,
                 hover_data=['CustomerClass', 'Count', 'MeanRecency', 'MeanFrequency', 'MeanMonetary'],
                 labels=labels)
fig2.update_layout(title='RFM Scatter Plot')

fig3 = px.bar(df, x="MeanRecency", y="CustomerClass", orientation='h', color='CustomerClass',
              color_discrete_sequence=color_sequence,
              category_orders = category_orders,
              labels=labels)
fig3.update_layout(title='Average Recency (days) by Customer Class', showlegend=False)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.write(fig1)

    with col2:
        st.write(fig2)

with st.container():
    col3, col4 = st.columns(2)

    with col3:
        st.write(fig3)

    with col4:
        st.write(df)