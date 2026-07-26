import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = "Biomass Potentials and Availibility Drivers",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Biomass Potential and Availibility Drivers')
st.subheader('Key Drivers:')

if "selected_driver" not in st.session_state:
    st.session_state.selected_driver = None

#create columns
empty_space, pestel_tabs = st.columns([2,6])

with empty_space:
    st.write("")

with pestel_tabs:
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
            with st.popover("Crop Yield"):
                st.markdown("some words here")
            #if st.button("Crop Yield", key = "one"):
                #st.session_state.selected_driver = "Crop Yield"
        with c2:
            with st.popover("Population"):
                st.markdown("some text here")
            #st.button("Population", key = "two")
        with c3:
            with st.popover("Forest Area"):
                st.markdown("some text here")
            #st.button("Forest Area", key = "three")

with st.container(border=True):
    left, right = st.columns([2,6])

    with left:
        st.markdown("Agricultural Biomass and Residues")
    with right:
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.popover("Crop Yield"):
                st.markdown("some words here")
            #st.button("Crop Yield", key = "four")
        with c2:
            with st.popover("Population"):
                st.markdown("some text here")
            #st.button("Population", key = "five")
        with c3:
            with st.popover("Forest Area"):
                st.markdown("some text here")
            #st.button("Forest Area", key = "six")

with st.container(border=True):
    left, right = st.columns([2,6])

    with left:
        st.markdown("Livestock Residues")
    with right:
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.popover("Crop Yield"):
                st.markdown("some words here")
            #st.button("Crop Yield", key = "seven")
        with c2:
            with st.popover("Population"):
                st.markdown("some text here")
            #st.button("Population", key = "eight")
        with c3:
            with st.popover("Forest Area"):
                st.markdown("some text here")
            #st.button("Forest Area", key = "nine")

st.markdown("---")
st.subheader("Driver Information")

with st.container(border = True):
    if st.session_state.selected_driver is None:
        st.info("Click on a driver above to view its information.")
    elif st.session_state.selected_driver == "Crop Yield":
        st.subheader("Crop Yield")
        st.caption("Type: Environmental")
        st.write("Crop yield is influenced by ___")


