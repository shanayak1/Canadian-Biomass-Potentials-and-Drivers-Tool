import streamlit as st

#page setup
home_page = st.Page(
    page="pages/home.py",
    title="Biomass Potential",
    icon=":material/account_circle:",
    default = True,
)

potential_page = st.Page(
    page="pages/potential.py",
    title = "Biomass Potentials",
    icon = ":material/bar_chart:",
)

bc_page = st.Page(
    page = "pages/bc.py",
    title = "British Columbia",
    icon = ":material/bar_chart:",
)

#navigation menu

pg = st.navigation(pages=[home_page, potential_page])

# navigation with sections
pg = st.navigation(
    {
        "Introductions": [home_page],
        "Alberta": [potential_page],
        "British Columbia": [bc_page],
    }
)

#yes
#run navigation

pg.run()

#shared on all pages
#st.logo("assets/")

