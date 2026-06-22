import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Alberta Biomass Potentials and Availability Data",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Alberta Biomass Potentials and Availability Data')
st.subheader('subtitle')

#load dataframe so our excel worksheet data
excel_file = 'data.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name = sheet_name,
                   usecols = 'B:F',
                   header = 2)

st.sidebar.header("Filters")

categories = df["Category"].unique()

selected_categories = st.multiselect(
    "Select Catgeory",
    categories,
    default = categories
)

subcategories = df[
    df["Category"].isin(selected_categories)
]["SubCategory"].unique()

selected_subcategories = st.multiselect(
    "Select SubCategory",
    subcategories,
    default = subcategories
)

min_sf = float(df["Sustainable Factor"].min())
max_sf = float(df["Sustainable Factor"].max())

selected_sf = st.slider(
    "Sustainable Factor",
    min_sf,
    max_sf,
    (min_sf, max_sf)
)

filtered_df = df[
    (df["Category"].isin(selected_categories))
    &
    (df["SubCategory"].isin(selected_subcategories))
    &
    (df["Sustainable Factor"] >= selected_sf[0])
    &
    (df["Sustainable Factor"] <= selected_sf[1])
]

fig = px.bar(
    filtered_df,
    x = "SubCategory",
    y = "Production Volume",
    color = "Category",
    title = "Production Volume by Biomass Subtype"
)

st.plotly_chart(fig, use_container_width = True)
