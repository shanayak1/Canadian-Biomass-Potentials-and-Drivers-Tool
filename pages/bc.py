import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "British Columbia Biomass Potentials and Availability Data",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('British Columbia Biomass Potentials and Availability Data')
st.subheader('Current Availability as of 2025')

#load dataframe so our excel worksheet data
excel_file = 'data.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name = sheet_name,
                   usecols = 'B:D',
                   header = 2)

st.sidebar.header("Filters")

categories = df["Category"].unique()

selected_categories = st.sidebar.multiselect(
    "Select Catgeory",
    categories,
    default = categories
)

subcategories = df[
    df["Category"].isin(selected_categories)
]["SubCategory"].unique()

selected_subcategories = st.sidebar.multiselect(
    "Select SubCategory",
    subcategories,
    default = subcategories
)


selected_sf = st.sidebar.slider(
    "Sustainable Removal Factor",
    min_value = 0.0,
    max_value = 3.0,
    value = 1.50,
    step = 0.10
)

filtered_df = df[
    (df["Category"].isin(selected_categories))
    &
    (df["SubCategory"].isin(selected_subcategories))
    
].copy()

filtered_df["Sustainable Potential"] = (
    filtered_df["Production Volume"]
    * selected_sf
)

fig = px.bar(
    filtered_df,
    x = "SubCategory",
    y = "Sustainable Potential",
    color = "Category",
    title = "Production Volume by Biomass Subtype"
)

st.plotly_chart(fig, use_container_width = True)

st.subheader('Future Biomass Availability Prediction')