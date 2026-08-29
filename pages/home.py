import streamlit as st
import pandas as pd

st.title("Biomass Potentials Tool")

st.subheader("A Brief Introduction and Methodology")

st.text("This tool has been created to build a better understanding of current biomass resources available in parts of Canada, as well as how these resource quantities will change in the future. To understand the key socio-economic and environmental drivers impacting biomass potential, the PESTEL (Political, Economic, Social, Technological, Environmental, Legal) framework. This tool will bring awareness to the current quantities of biomass resource within the provinces chosen in the scope of this project, detailing the energy potential available by province. This data helps to inform comparisions between how different provinces contribute to the greater biomass supply across the country, as well as discuss the factors that impact that biomass supply.")

definitions_df = pd.DataFrame({
    "Term": [
        "Bioeconomy",
        "Biomass",
        "Dry Matter",
        "Theoretical Potential",
        "Technical Potential",
        "Sustainable Potential",
        "Energy Potential",
    ],
    "Definition":[
        "The bioeconomy is defined as the economic activity associated with the invention, development, production and use of primarily bio-based products, bio-based production processes and/or biotechnology-based intellectual property. ",
        "Biomass is organic material originating from plant and animal sources. Organic materials embedded in geological formations and/or fossilized are not considered biomass",
        "Dry matter is biomass excluding its water contents. Can be calculated using Dry Mass = Biomass mass * (1- (moisture content/100)) where biomass mass is measured in tons and moisture content is a percentage.",
        "Theoretical potential refers to the total residue production of aboveground biomass without taking into consideration any harvesting, environmental or economic constraints.",
        "Technical potential refers to the physical amount of materials that could be technically removed from the field. This will depend on crop type, efficiency of equipment and field management factors.",
        "Sustainable potential refers to the physical amount of materials that could be removed from the field considering technical constraints for harvesting and environmental impacts on the land.",
        "Energy potential is the energy produced by the harvested biomass quantities",
    ]
})

st.subheader("Terminology")
st.text("The following terminology is used frequently throughout the biomass potentials and drivers tool:")


with st.container():
    st.table(definitions_df)


