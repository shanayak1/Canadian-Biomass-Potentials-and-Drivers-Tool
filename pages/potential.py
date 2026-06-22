import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Alberta Biomass Potentials and Availability Data",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Albertan biomass potentials')
st.subheader('blah blah blah')

#load dataframe so our excel worksheet data
excel_file = 'data.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name = sheet_name,
                   usecols = 'B:D',
                   header = 2)

biomass_category = df['Category'].unique().tolist()
subtypes = df['SubCategory'].unique().tolist()

#sus_factor = st.slider('sustainable factor', min_value=min)

biomass_selection = st.multiselect('Category:',
                                   biomass_category,
                                   default = biomass_category)

st.dataframe(df)

#filter dataframe based on user selection
mask = (df['Category'].isin(biomass_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'#Available Results: {number_of_result}*')

#group dataframe
df_grouped = df[mask].groupby(by=['Category']).count()[['SubCategory']]
df_grouped = df_grouped.rename(columns={'SubCategory': 'BLAH'})
df_grouped = df_grouped.reset_index()

#plot bar chart
bar_chart = px.bar(df.grouped,
                   x = 'Category',
                   y = 'Production Volume',
                   text = 'Production Volume',
                   color_discrete_sequence = ['#F63366']*len(df.grouped),
                   template = 'plotly_white')

st.plotly_chart(bar_chart)