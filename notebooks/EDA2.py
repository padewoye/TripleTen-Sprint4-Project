import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats as sp

df = pd.read_csv('../datasets/vehicles_us.csv')
df.head(10)

st.header('Car Types by Manufacturer')
fig = px.histogram(df, x='model', color='type')
st.write(fig)

