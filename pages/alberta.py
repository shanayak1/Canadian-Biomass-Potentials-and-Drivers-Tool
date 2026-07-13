import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Alberta Biomass Potentials and Availability Data",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Alberta Biomass Potentials and Availability Data')
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

sf_dict = {}

if "Forestry" in selected_categories:
    forestry_sf = st.sidebar.slider(
        "Forestry Sustainable Removal Factor",
        min_value = 46.00,
        max_value = 72.00,
        value = 59.0,
        step = 1.0
    )
    sf_dict["Forestry"] = forestry_sf

if "Purpose Grown Energy Crops" in selected_categories:
    crop_sf = st.sidebar.slider(
        "Purpose Grown Energy Crops Sustainable Removal Factor",
        min_value = 25.00,
        max_value = 50.00,
        value = 32.0,
        step = 1.0
    )
    sf_dict["Purpose Grown Energy Crops"] = crop_sf

livestock_sf_dict = {
    "Sheep and Lambs" : 0.3,
    "Calves (under 1 year)" : 0.82,
    "Dairy cows" : 0.82,
    "Steers (1 year and over)": 0.82,
    "Bulls" : 0.5,
    "Beef heifers" : 0.5,
    "Dairy heifers" : 0.8,
    "Boars" : 1,
    "Slaughter heifers" : 0.6,
    "Sows and gilts" : 1,
    "Pigs" : 1,
    "Beef cows" : 0.5,
}

#filter all the rows to only have selected categories/subcategories
filtered_df = df[
    (df["Category"].isin(selected_categories))
    &
    (df["SubCategory"].isin(selected_subcategories))
].copy()

#filter them to the selected sustainable removal factor
filtered_df["Sustainable Removal Factor"] = (
    filtered_df["Category"].map(sf_dict)
)

#sub in the new livestock sus factor
livestock_rows = filtered_df["Category"] == "Livestock Residue"

#sub in new crop sus factor

#sub in livestock factor into dataframe
filtered_df.loc[livestock_rows, "Sustainable Removal Factor"] = (
    filtered_df.loc[livestock_rows, "SubCategory"].map(livestock_sf_dict)
)

#calculate all sustainable potentials
filtered_df["Sustainable Potential"] = (
    filtered_df["Production Volume"]
    * filtered_df["Sustainable Removal Factor"]
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