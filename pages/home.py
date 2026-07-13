import streamlit as st

st.title("Biomass Potentials Tool")

st.subheader("A Brief Introduction and Methodology")

st.text("This tool has been created to build a better understanding of current biomass resources available in parts of Canada, as well as how these resource quantities will change in the future. The following drivers were identified as factors that affect biomass resource availability in the future")

st.subheader("Biomass Availability Drivers")

left_column, right_column = st.columns(2)

left_column.text("Forestry")

right_column.write("Livestock Residue")
