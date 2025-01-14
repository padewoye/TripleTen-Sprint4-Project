import streamlit as st
import pandas as pd
import plotly.express as px

# Project Section #1:  Data Viewer
#     1)  Load/Read the dataset from the given csv file
#     2)  Re-order the dataframe columns for better User Viewing experience 
#     3)  Cleanup the MODEL column data by capitalizing, replacing names to popular conventions (e.g. Bmw = BMW)
#     4)  Sort the data by MODEL column
#     5)  Add a Select All checkbox to display all MODELS
#     6)  Add a selector dropdown box to filter by MODEL
#     7)  Add Data Viewer for dataset display
# 

# 1-1
df = pd.read_csv('datasets/vehicles_us.csv')

# 1-2
st.header('Data Viewer - Car Sale Advertisements')
df = df[['model', 'model_year', 'price', 'date_posted', 'days_listed', 'odometer', 'transmission', 'fuel', 'condition', 'cylinders', 'type', 'paint_color', 'is_4wd']]

# 1-3
df['model'] = df['model'].str.title()
substitutes = {'Bmw X5': 'BMW X5', 'Gmc Sierra 1500': 'GMC Sierra 1500', 'Honda Cr-V': 'Honda CR-V', 'Gmc Sierra': 'GMC Sierra'}
df['model'] = df['model'].replace(substitutes)

# 1-4
df.sort_values(by='model', ascending=True, inplace=True)
df = df.reset_index(drop=True)

# 1-5
select_all = st.checkbox('Select All:')

# 1-6
model_selector = df['model'].unique()
model_dropbox = st.selectbox('Select a Model to Filter: ', model_selector)

# 1-7
if select_all:
    df_filter_model = df
    df_filter_model
else:
    df_filter_model = df[df['model'] == model_dropbox]
    df_filter_model

# Project Section #2:  Histograms to view data from different perspectives
#     1)  Add Histogram of Vehicle Model Count by Type
#     2)  Add Histogram of Model Year Count by Vehicle Condition
#     3)  Add Histogram of Model Year Count by Paint Color

# 2-1
st.header('Hist A - Vehicle Model Count by Type')
st.write("""
###### Select/Unselect the (multiple or single) Type to FILTER the Data View
""" )
fig = px.histogram(df, x='model', color='type')
st.write(fig)

# 2-2
st.header('Hist B - Model Year Count by Vehicle Condition')
st.write("""
###### Select/Unselect the (multiple or single) Condition to FILTER the Data View
""" )
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)

# 2-3
st.header('Hist C - Model Year Count by Paint Color')
st.write("""
###### Select/Unselect the (multiple or single) Paint Color to FILTER the Data View
""" )
fig = px.histogram(df, x='model_year', color='paint_color')
st.write(fig)

# Project Section #3:  Histogram and Plot to view data from Price perspectives
#     1)  Add Price Distribution between Models
#     2)  Add Price Scatterplot across Age per Model

# 3-1
st.header('Hist D - Price Distribution between Models')
default_index = 1

model_price_selector1 = df['model'].unique()
model_dropbox1 = st.selectbox('Select first Model: ', model_price_selector1)
df_model1 = df[df['model'] == model_dropbox1]

model_price_selector2 = df['model'].unique()
model_dropbox2 = st.selectbox('Select second Model: ', model_price_selector2, index=default_index)
df_model2 = df[df['model'] == model_dropbox2]

df_merged = pd.concat([df_model1, df_model2], axis=0)
fig = px.histogram(df_merged, x='price', color='model')
st.write(fig)

# 3-2
df['age'] = 2024 - df['model_year']
st.header('Scatter Plot - Price Distribution Across Age per Model')
fig = px.scatter(df, x='price', y='age', color='model')
st.write(fig)