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

if "Forestry Residue" in selected_categories:
    forestry_sf = st.sidebar.slider(
        "Forestry Residue Factor",
        min_value = 46.00,
        max_value = 72.00,
        value = 59.0,
        step = 1.0
    )
    sf_dict["Forestry Residue"] = forestry_sf

sf_dict["Forestry Biomass"] = 1.0

crops_dict = {}

if "Crop Residue" in selected_categories:
    if "Wheat" in selected_subcategories:
        wheat_sf = st.sidebar.slider(
            "Wheat Residue Factor",
            min_value = 25.0,
            max_value = 50.0,
            value = 37.0,
            step = 1.0,
        )
        crops_dict["Wheat"] = wheat_sf
    if "Canola" in selected_subcategories:
        canola_sf = st.sidebar.slider(
            "Canola Residue Factor",
            min_value = 30.0,
            max_value = 50.0,
            value = 40.0,
            step = 1.0,
        )
        crops_dict["Canola"] = canola_sf
    if "Barley" in selected_subcategories:
        barley_sf = st.sidebar.slider(
            "Barley Residue Factor",
            min_value = 25.0,
            max_value = 50.0,
            value = 37.0,
            step = 1.0,
        )
        crops_dict["Barley"] = barley_sf
    if "Lentils" in selected_subcategories:
        lentil_sf = st.sidebar.slider(
            "Lentils Residue Factor",
            min_value = 25.0,
            max_value = 40.0,
            value = 32.0,
            step = 1.0,
        )
        crops_dict["Lentils"] = lentil_sf
    if "Corn" in selected_subcategories:
        corn_sf = st.sidebar.slider(
            "Corn Residue Factor",
            min_value = 30.0,
            max_value = 60.0,
            value = 45.0,
            step = 1.0,
        )
        crops_dict["Corn"] = corn_sf
    if "Oats" in selected_subcategories:
        oat_sf = st.sidebar.slider(
            "Oats Residue Factor",
            min_value = 30.0,
            max_value = 50.0,
            value = 40.0,
            step = 1.0,
        )
        crops_dict["Oats"] = oat_sf
    if "Soybean" in selected_subcategories:
        soybean_sf = st.sidebar.slider(
            "Soybean Residue Factor",
            min_value = 25.0,
            max_value = 50.0,
            value = 37.0,
            step = 1.0,
        )
        crops_dict["Soybean"] = soybean_sf
    if "Rye" in selected_subcategories:
        rye_sf = st.sidebar.slider(
            "Rye Residue Factor",
            min_value = 30.0,
            max_value = 50.0,
            value = 40.0,
            step = 1.0,
        )
        crops_dict["Rye"] = rye_sf
    if "Dry Beans" in selected_subcategories:
        dry_sf = st.sidebar.slider(
            "Dry Beans Residue Factor",
            min_value = 25.0,
            max_value = 40.0,
            value = 32.0,
            step = 1.0,
        )
        crops_dict["Dry Beans"] = dry_sf
    if "Flaxseed" in selected_subcategories:
        flaxseed_sf = st.sidebar.slider(
            "Flaxseed Residue Factor",
            min_value = 30.0,
            max_value = 40.0,
            value = 35.0,
            step = 1.0,
        )
        crops_dict["Flaxseed"] = flaxseed_sf
    if "Dry Peas" in selected_subcategories:
        peas_sf = st.sidebar.slider(
            "Dry Peas Residue Factor",
            min_value = 25.0,
            max_value = 35.0,
            value = 30.0,
            step = 1.0,
        )
        crops_dict["Dry Peas"] = peas_sf
    if "Mustard Seed" in selected_subcategories:
        mustard_sf = st.sidebar.slider(
            "Mustard Seed Residue Factor",
            min_value = 20.0,
            max_value = 40.0,
            value = 30.0,
            step = 1.0,
        )
        crops_dict["Mustard Seed"] = mustard_sf

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
crop_rows = filtered_df["Category"] == "Crop Residue"
filtered_df.loc[crop_rows, "Sustainable Removal Factor"] = (
    filtered_df.loc[crop_rows, "SubCategory"].map(crops_dict)
)

#calculate all sustainable potentials
filtered_df["Sustainable Potential (Dry Matter Tonnes)"] = (
    filtered_df["Production Volume"]
    * filtered_df["Sustainable Removal Factor"]
)

st.dataframe(filtered_df)

category_energy_df = (
    filtered_df
    .groupby("Category", as_index=False)
    .agg({
        "Sustainable Potential (Dry Matter Tonnes)":"sum"
    })
)

st.dataframe(category_energy_df)

lhv = {
    "Forestry Biomass": 0.00001796,
    "Forestry Residue": 0.00001915,
    "Purpose Grown Energy Crops":0.00001758,
    "Crop Residue": 0.00001722,
    "Livestock Residue":0.00001108,
    "Urban Waste": 0.0000171,
}

category_energy_df["LHV"] = (
    category_energy_df["Category"].map(lhv)
)
#calculate energy
category_energy_df["Energy Potential (PJ)"] = (
    category_energy_df["Sustainable Potential (Dry Matter Tonnes)"]
    * category_energy_df["LHV"]
)

#plot energy potential graph
energy_fig = px.bar(
    category_energy_df,
    x = "Category",
    y = "Energy Potential (PJ)",
    color = "Category",
    color_discrete_map = {
        "Forestry" : "#4D8C57",
        "Livestock Residue" : "#78A161",
        "Purpose Grown Energy Crops" : "#A3B56B",
        "Urban Waste" : "#895129",
        "Crop Residue" : "#F8DE7E",
    },
    title = "Biomass Energy Potential"
)

st.plotly_chart(
    energy_fig,
    use_container_width = True
)



fig = px.bar(
    filtered_df,
    x = "SubCategory",
    y = "Sustainable Potential (Dry Matter Tonnes)", 
    color = "Category",
    color_discrete_map = {
        "Forestry" : "#4D8C57",
        "Livestock Residue" : "#78A161",
        "Purpose Grown Energy Crops" : "#A3B56B",
        "Urban Waste" : "#895129",
        "Crop Residue" : "#F8DE7E",
    },
    title = "Production Volume by Biomass Subtype",
)
    

st.plotly_chart(fig, use_container_width = True)

st.dataframe(
    category_energy_df[
        ["Category",
         "Sustainable Potential (Dry Matter Tonnes)",
         "Energy Potential (PJ)"]
    ]
)