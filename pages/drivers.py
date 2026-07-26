import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Biomass Potentials and Availibility Drivers",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Biomass Potential and Availibility Drivers')
st.subheader('Key Drivers:')

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


#create rows using a container
with st.container(border=True):
    left, right = st.columns([2,6])

    with left:
        st.markdown("Forestry Biomass and Residues")
    with right:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("Crop Yield", key = "one")
        with c2:
            st.button("Population", key = "two")
        with c3:
            st.button("Forest Area", key = "three")

with st.container(border=True):
    left, right = st.columns([2,6])

    with left:
        st.markdown("Agricultural Biomass and Residues")
    with right:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("Crop Yield", key = "four")
        with c2:
            st.button("Population", key = "five")
        with c3:
            st.button("Forest Area", key = "six")

with st.container(border=True):
    left, right = st.columns([2,6])

    with left:
        st.markdown("Livestock Residues")
    with right:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("Crop Yield", key = "seven")
        with c2:
            st.button("Population", key = "eight")
        with c3:
            st.button("Forest Area", key = "nine")





#create popup display
#with st.popover("Crop Y"):
    #st.markdown("WORDS HERE")

