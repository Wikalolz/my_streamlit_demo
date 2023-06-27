import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import seaborn as sns

# Load some data
df = pd.read_csv('/data/20200306_hundehalter.csv')

# Add title and header
st.title("Introduction to Streamlit")
st.header("Dog Zurich")

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.header("This is my dataset:")
    st.dataframe(data=df)
    # st.table(data=df)
    # st.write(data=df)

# Setting up columns
left_column, middle_column, right_column = st.columns([2, 2, 1])

#graph gender

fig = px.bar(df, x ='GESCHLECHT', title= 'Gender of the owner')
st.plotly_chart(fig, sharing="streamlit", theme="streamlit")

#graph age

fig1 = px.bar(df, x ='ALTER', title= 'Nb of dog per age tranche')
fig1.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig1, sharing="streamlit", theme="streamlit")

#graph kreis
df_kreis_mod = df['STADTKREIS'].astype(str)
fig2 = px.bar(df_kreis_mod, x ='STADTKREIS', title= 'Nb of dog per kreis')
fig2.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig2, sharing="streamlit", theme="streamlit")

# Widgets: selectbox
kreis = sorted(pd.unique(df['STADTKREIS']))
kreis = st.selectbox("Choose a kreis", kreis)

#graph1
df_kreis= df[df["STADTKREIS"]== kreis]
fig3= px.bar(df_kreis, x ='ALTER')
fig3.update_layout(xaxis={'categoryorder':'total descending'})

st.plotly_chart(fig3, use_container_width=False, sharing="streamlit", theme="streamlit")


