import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Biomass Potentials and Availibility Drivers",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Biomass Potential and Availibility Drivers')
st.subheader('Key Drivers:')

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


