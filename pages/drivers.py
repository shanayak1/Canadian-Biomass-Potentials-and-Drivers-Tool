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
    st.button("Crop Yield")
with st.container(border=True):
    st.write("Agricultural Biomass and Residues")
with st.container(border=True):
    st.write("Livestock Residues")   

#create columns
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.button("Political", use_container_width = True)
with col2:
    st.button("Environmental", use_container_width = True)
with col3:
    st.button("Social", use_container_width = True)
with col4:
    st.button("Technological", use_container_width = True)
with col5:
    st.button("Eco", use_container_width = True)
with col6:
    st.button("Legal", use_container_width = True)

if "selected_driver" not in st.session_state:
    st.session_state.selected_driver = None

#create popup display
with st.popover("Crop Y"):
    st.markdown("WORDS HERE")

