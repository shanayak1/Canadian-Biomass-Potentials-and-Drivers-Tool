import streamlit as st

st.title("Biomass Potentials Tool")

st.subheader("A Brief Introduction and Methodology")

st.text("""
This tool has been created to build a better understanding of current biomass resources available 
in parts of Canada, as well as how these resource quantities will change in the future. To understand 
the key socio-economic and environmental drivers impacting biomass potential, the PESTEL 
(Political, Economic, Social, Technological, Environmental, Legal) framework. This framework 
""")



# Prior research conducted creates a status quo meta database of biomass resource 
# use within Canada, establishing the status quo of biomass residue and waste. My 
# research will focus on analyzing the driving forces of future biomass potentials, 
# using the current status quo within Canada to develop a tool that assesses future 
# potential. This tool will involve a user interface where the user can adapt the 
# drivers based on their specific needs or focuses. The program will contain data regarding the current status 
# quo of biomass resources, current utilization rates as well as the quantitative factors 
# determined from PESTEL research. This data will be contained using CSV files in a 
# python-based terminal. The program will use the predeveloped status quo as the baseline 
# scenario and utilize PESTEL factors to map potentials and display the results in tables, 
# as well as graphs displaying biomass potential over time and provincial comparisons. 
# This tool will aid large provincial and municipal bodies in assessing how the province 
# and country can proceed with climate projects while keeping biomass resources in mind to
#  improve the climate and reduce our environmental impact.