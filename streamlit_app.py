import streamlit as st

#page setup
home_page = st.Page(
    page="pages/home.py",
    title="Intro to Biomass",
    icon=":material/account_circle:",
    default = True,
)

potential_page = st.Page(
    page="pages/potential.py",
    title = "Biomass Potentials",
    icon = ":material/bar_chart:",
)

#navigation menu

pg = st.navigation(pages=[home_page, potential_page])

# navigation with sections
pg = st.navigation(
    {
        "Info": [home_page],
        "projects": [potential_page]
    }
)


#run navigation

pg.run()

