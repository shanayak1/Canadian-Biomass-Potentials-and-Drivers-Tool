import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Alberta Biomass Potentials and Availability Data",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Albertan biomass potentials')
st.subheader('subtitle')

#load dataframe so our excel worksheet data
excel_file = 'data.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name = sheet_name,
                   usecols = 'B:F',
                   header = 2)

biomass_category = df['Category'].unique().tolist()
subtypes = df['SubCategory'].unique().tolist()
sus_factors = df['Sustainable Factor'].unique().tolist()

sus_factor_selection = st.slider('Sustainable Factor:',
                                min_value = min(sus_factors),
                                max_value = max(sus_factors),
                                value = (min(sus_factors),max(sus_factors)))

biomass_selection = st.multiselect('Category:',
                                   biomass_category,
                                   default = biomass_category)

subcategory = st.multiselect('SubCategory:',
                             subtypes,
                             default = subtypes)

st.dataframe(df)

#filter dataframe based on user selection
mask = (df['Sustainable Factor'].between(*sus_factor_selection)) & (df['Category'].isin(biomass_selection)) & (df['SubCategory'].isin(subcategory))
number_of_result = df[mask].shape[0]
st.markdown(f'#Available Results: {number_of_result}*')

#group dataframe
df_grouped = df[mask].groupby(by=['Production Volume']).count()[['Sustainable Factor']]
#df_grouped = df_grouped.rename(columns={'SubCategory': 'Biomass subtypes'})
df_grouped = df_grouped.reset_index()

#plot bar chart
bar_chart = px.bar(df_grouped,
                   x = 'Sustainable Factor',
                   y = 'Production Volume',
                   text = 'Production Volume',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template = 'plotly_white')

st.plotly_chart(bar_chart)