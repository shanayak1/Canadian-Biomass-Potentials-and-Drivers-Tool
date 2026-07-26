import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Biomass Potentials and Availibility Drivers",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Biomass Potential and Availibility Drivers')
st.subheader('Key Drivers:')


tabs = st.tabs([
    "Political",
    "Environmental",
    "Social",
    "Technological",
    "Ecological",
    "Legal",
])

#create rows using a container
with st.container(border=True):
    st.write("Forestry Biomass and Residues")
with st.container(border=True):
    st.write("Agricultural Biomass and Residues")
with st.container(border=True):
    st.write("Livestock Residues")   

#create columns
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Crop Yield"):
        st.session_state.selected_driver = "Crop Yield"
with col2:
    if st.button("City Population"):
        st.session_state.selected_driver = "City Population"

if "selected_driver" not in st.session_state:
    st.session_state.selected_driver = None

#create popup display
if st.session_state.selected_driver == "Crop Yield":
    with st.container(border = True):
        st.subheader("Crop Yield")
        st.caption ("Environmental")
        st.write("Crop yield is ______")

