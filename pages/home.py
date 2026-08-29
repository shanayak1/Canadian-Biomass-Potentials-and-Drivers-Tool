import streamlit as st
import pandas as pd

st.title("Biomass Potentials Tool")

st.subheader("A Brief Introduction and Methodology")

st.text("This tool has been created to build a better understanding of current biomass resources available in parts of Canada, as well as how these resource quantities will change in the future. To understand the key socio-economic and environmental drivers impacting biomass potential, the PESTEL (Political, Economic, Social, Technological, Environmental, Legal) framework. This tool will bring awareness to the current quantities of biomass resource within the provinces chosen in the scope of this project, detailing the energy potential available by province. This data helps to inform comparisions between how different provinces contribute to the greater biomass supply across the country, as well as discuss the factors that impact that biomass supply.")

st.subheader("Terminology")

st.text("The following terminology is used frequently throughout the biomass potentials and drivers tool:")

definitions_df = pd.DataFrame({
    "Term": [
        "Bioeconomy",
        "Biomass",
        "Feedstock",
    ],
    "Definition":[
        "blah",
        "blehhh",
        "blooh",
    ]
})

with st.container():
    st.subheader("Terminology")
    
    st.dataframe(
        definitions_df,
        hide_index = True,
        use_container_width = True,
        column_config = {
            "Term": st.column_config.TextColumn(
                "Term",
                width = 250
            ),
            "Definition": st.column_config.TextColumn(
                "Definition",
                width = "large"
            )
        }

    )


