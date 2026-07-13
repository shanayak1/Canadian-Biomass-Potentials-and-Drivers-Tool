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

st.sidebar.subheader("Sustainable Removal Factors (%):")

if "Forestry" in selected_categories:
    forestry_sf = st.sidebar.slider(
        "Forestry Factor",
        min_value = 46.00,
        max_value = 72.00,
        value = 59.0,
        step = 1.0
    )
    sf_dict["Forestry"] = forestry_sf

crops_dict = {}

if "Purpose Grown Energy Crops" in selected_categories:
    if "Wheat" in selected_subcategories:
        wheat_sf = st.sidebar.slider(
            "Wheat Factor",
            min_value = 25.0,
            max_value = 50.0,
            value = 37.0,
            step = 1.0,
        )
        crops_dict["Wheat"] = wheat_sf
    if "Canola" in selected_subcategories:
        canola_sf = st.sidebar.slider(
            "Canola Factor",
            min_value = 30.0,
            max_value = 50.0,
            value = 40.0,
            step = 1.0,
        )
        crops_dict["Canola"] = canola_sf
    if "Barley" in selected_subcategories:
        barley_sf = st.sidebar.slider(
            "Barley Factor",
            min_value = 25.0,
            max_value = 50.0,
            value = 37.0,
            step = 1.0,
        )
        crops_dict["Barley"] = barley_sf
    if "Lentils" in selected_subcategories:
        lentil_sf = st.sidebar.slider(
            "Lentils Factor",
            min_value = 25.0,
            max_value = 40.0,
            value = 32.0,
            step = 1.0,
        )
        crops_dict["Lentils"] = lentil_sf
    if "Corn" in selected_subcategories:
        corn_sf = st.sidebar.slider(
            "Corn Factor",
            min_value = 30.0,
            max_value = 60.0,
            value = 45.0,
            step = 1.0,
        )
        crops_dict["Corn"] = corn_sf
    if "oats" in selected_subcategories:
        oat_sf = st.sidebar.slider(
            "Oats Factor",
            min_value = 30.0,
            max_value = 50.0,
            value = 40.0,
            step = 1.0,
        )
        crops_dict["oats"] = oat_sf
    if "soybean" in selected_subcategories:
        soybean_sf = st.sidebar.slider(
            "Soybean Factor",
            min_value = 25.0,
            max_value = 50.0,
            value = 37.0,
            step = 1.0,
        )
        crops_dict["soybean"] = soybean_sf
    if "rye" in selected_subcategories:
        rye_sf = st.sidebar.slider(
            "Rye Factor",
            min_value = 30.0,
            max_value = 50.0,
            value = 40.0,
            step = 1.0,
        )
        crops_dict["rye"] = rye_sf
    if "dry beans" in selected_subcategories:
        dry_sf = st.sidebar.slider(
            "Dry Beans Factor",
            min_value = 25.0,
            max_value = 40.0,
            value = 32.0,
            step = 1.0,
        )
        crops_dict["dry beans"] = dry_sf
    if "flaxseed" in selected_subcategories:
        flaxseed_sf = st.sidebar.slider(
            "Flaxseed Factor",
            min_value = 30.0,
            max_value = 40.0,
            value = 35.0,
            step = 1.0,
        )
        crops_dict["flaxseed"] = flaxseed_sf
    if "dry peas" in selected_subcategories:
        peas_sf = st.sidebar.slider(
            "Dry Peas Factor",
            min_value = 25.0,
            max_value = 35.0,
            value = 30.0,
            step = 1.0,
        )
        crops_dict["dry peas"] = peas_sf
    if "mustard seed" in selected_subcategories:
        mustard_sf = st.sidebar.slider(
            "Mustard Seed Factor",
            min_value = 20.0,
            max_value = 40.0,
            value = 30.0,
            step = 1.0,
        )
        crops_dict["mustard seed"] = mustard_sf

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

urban_waste_dict = {
    "Sewage" : 0.9,
    "Biosolids" : 0.9,
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

#sub in livestock factor into dataframe
filtered_df.loc[livestock_rows, "Sustainable Removal Factor"] = (
    filtered_df.loc[livestock_rows, "SubCategory"].map(livestock_sf_dict)
)

#sub in new urban waste sus factor
urban_rows = filtered_df["Category"] == "Urban Waste"
filtered_df.loc[urban_rows, "Sustainable Removal Factor"] = (
    filtered_df.loc[urban_rows, "SubCategory"].map(urban_waste_dict)
)

#sub in new crop sus factors
crop_rows = filtered_df["Category"] == "Purpose Grown Energy Crops"
filtered_df.loc[crop_rows, "Sustainable Removal Factor"] = (
    filtered_df.loc[crop_rows, "SubCategory"].map(crops_dict)
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