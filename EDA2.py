import streamlit as st
import pandas as pd
import plotly.express as px

# Project Section #1:
#     1)  Load/Read the dataset from the given csv file
#     2)  Add Data Viewer for dataset display
#     3)  Re-order the dataframe columns for better User Viewing experience 
#     4)  Cleanup the MODEL column data by capitalizing, replacing names to popular conventions (e.g. Bmw = BMW)
#     5)  Sort the data by MODEL column
#     6)  Add a selector dropdown box to filter by MODEL
#     7)  Add a Select All checkbox to display all MODELS
# 

df = pd.read_csv('datasets/vehicles_us.csv')

st.header('Car Sale Advertisement Data Viewer')

df = df[['model', 'model_year', 'price', 'date_posted', 'days_listed', 'odometer', 'transmission', 'fuel', 'condition', 'cylinders', 'type', 'paint_color', 'is_4wd']]
df['model'] = df['model'].str.title()

substitutes = {'Bmw X5': 'BMW X5', 'Gmc Sierra 1500': 'GMC Sierra 1500', 'Honda Cr-V': 'Honda CR-V', 'Gmc Sierra': 'GMC Sierra'}
df['model'] = df['model'].replace(substitutes)
df.sort_values(by='model', ascending=True, inplace=True)
df = df.reset_index(drop=True)

select_all = st.checkbox('Select All:')
model_selector = df['model'].unique()
model_dropbox = st.selectbox('Select a Model to Filter: ', model_selector)

if select_all:
    df_filter_model = df
    df_filter_model
else:
    df_filter_model = df[df['model'] == model_dropbox]
    df_filter_model

