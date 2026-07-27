import streamlit as st

#page setup
home_page = st.Page(
    page="pages/home.py",
    title="Biomass Potential",
    icon=":material/account_circle:",
    default = True,
)

alberta_page = st.Page(
    page="pages/alberta.py",
    title = "Biomass Potential",
    icon = ":material/bar_chart:",
)

bc_page = st.Page(
    page = "pages/bc.py",
    title = "Biomass Potential",
    icon = ":material/bar_chart:",
)

drivers_page = st.Page(
    page = "pages/drivers.py",
    title = "Drivers of Biomass Potential",
    icon = ":material/bar_chart:",
)

#navigation menu

pg = st.navigation(pages=[home_page, alberta_page])

# navigation with sections
pg = st.navigation(
    {
        "Introductions": [home_page],
        "Biomass Potentials": [alberta_page, bc_page],
        "Biomass Drivers": [drivers_page],
    }
)

#yes
#run navigation

pg.run()

#shared on all pages
#st.logo("assets/")

