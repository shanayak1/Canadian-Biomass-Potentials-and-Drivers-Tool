import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#configure the page setup
st.set_page_config(page_title = "Biomass Potentials and Availibility Drivers",
                   page_icon = ":bar_chart:",
                   layout="wide")

st.header('Biomass Potential and Availibility Drivers')
st.subheader('Key Drivers:')

#set session state
if "selected_driver" not in st.session_state:
    st.session_state.selected_driver = None

#create pestel tabs
t1, t2, t3, t4, t5, t6 = st.tabs(["Political", "Economic", "Social", "Technological", "Environmental", "Legal"])

with t6:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
            # with right:
            #     c1 = st.columns(1)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
                
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
            # with right:
            #     c1 = st.columns(1)
           
with t5:
    with st.container(border=True):
        left, right = st.columns([2,6])
    with left:
        st.markdown("Forestry Biomass and Residues")
    with right:
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            with st.popover("Afforestation"):
                st.markdown("some text here")
        with c2:
            with st.popover("Deforestation"):
                st.markdown("a description")
        with c3:
            with st.popover("Land Availability"):
                st.markdown("description")
        with c4:
            with st.popover("Forest Fire"):
                st.markdown("description")
        with c5:
            with st.popover("Disease"):
                st.markdown("description")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
        with right:
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                with st.popover("Crop Yield"):
                    st.markdown("some text here")
            with c2:
                with st.popover("Cropland"):
                    st.markdown("a description")
            with c3:
                with st.popover("Land Availability"):
                    st.markdown("description")
            with c4:
                with st.popover("Extreme Weather"):
                    st.markdown("description")
            with c5:
                with st.popover("Climate Change"):
                    st.markdown("description")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residues")
            # with right:
            #     c1, c2, c3, c4, c5, c6 = st.columns(6)
with t4:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
        with right:
                # c1 = st.columns(1)
                # with c1:
            with st.popover("Farming Practices/Equipment"):
                st.markdown("some text here")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
        with right:
            with st.popover("Sustainable Removal Practices"):
                st.markdown("some text here")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
            # with right:
            #     c1 = st.columns(1)
with t3:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
        with right:
            with st.popover("Livestock Population"):
                st.markdown("""
                <style>
                div[data-testid="stPopover"] button {
                    background:"#87AE73";
                    color:#000000;
                    font-weight:bold;
                }
                </style>
                """, unsafe_allow_html=True)
                st.subheader("Livestock Population")
                st.caption("Type: Social")
                st.divider()
                st.markdown("""
            Crop yield is ___ and __ and influenced by _______.
                            
                            
            **As a Driver of Biomass Potential and Bioconversion**
            
            Higher crop yields directly increase the amount of biomass produced.
                            
                            
            **Explore further literature**
                            
            insert links here """)
                #st.markdown("some text here")
with t2:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
        with right:
                # c1 = st.columns(1)
                # with c1:
            with st.popover("Cost"):
                st.markdown("some text here")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
        with right:
                # c1 = st.columns(1)
                # with c1:
            with st.popover("Cost"):
                st.markdown("some text here")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
        with right:
                # c1 = st.columns(1)
                # with c1:
            with st.popover("Cost"):
                st.markdown("some text here")
with t1:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
            # with right:
            #     c1 = st.columns(1)
                
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
            # with right:
            #     c1 = st.columns(1)
            
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
            # with right:
            #     c1 = st.columns(1)

# with pestel_tabs:
#     col1, col2, col3, col4, col5, col6 = st.columns(6)
#     with col1:
#         st.button("Political", use_container_width = True)
#     with col2:
#         st.button("Economic", use_container_width = True)
#     with col3:
#         st.button("Social", use_container_width = True)
#     with col4:
#         st.button("Technological", use_container_width = True)
#     with col5:
#         st.button("Environmental", use_container_width = True)
#     with col6:
#         st.button("Legal", use_container_width = True)


#create rows using a container
# with st.container(border=True):
#     left, right = st.columns([2,6])

#     with left:
#         st.markdown("Forestry Biomass and Residues")
#     with right:
#         c1, c2, c3, c4, c5, c6 = st.columns(6)
        # with c1:
        #     #with st.popover("Crop Yield"):
        #         #st.markdown("some words here")
        #     #if st.button("Crop Yield", key = "one"):
        #         #st.session_state.selected_driver = "Crop Yield"
        #         st.write()
        # with c2:
        #     with st.popover("Cost"):
        #         st.markdown("some text here")
        # with c3:
        #     #with st.popover("erm"):
        #         #st.markdown("some text here")
        #     #st.button("Forest Area", key = "three")
        #     st.write()
        # with c4:
        #     with st.popover("Farming Practices/Equipment"):
        #         st.markdown("some text here")
        # with c5:
        #     with st.popover("Afforestation"):
        #         st.markdown("some text here")
        #     with st.popover("Deforestation"):
        #         st.markdown("a description")
        #     with st.popover("Land Availability"):
        #         st.markdown("description")
        #     with st.popover("Forest Fire"):
        #         st.markdown("description")
        #     with st.popover("Disease"):
        #         st.markdown("description")
#         with c6:
#             #with st.popover("smth"):
#                 #st.markdown("some text here")
            
#             st.write()
# with st.container(border=True):
#     left, right = st.columns([2,6])

#     with left:
#         st.markdown("Agricultural Biomass and Residues")
#     with right:
#         c1, c2, c3, c4, c5, c6 = st.columns(6)
#         # with c1:
#         #     #with st.popover("Crop Yield"):
#         #         #st.markdown("some words here")
#         #     #st.button("Crop Yield", key = "four")
#         #     st.write()
#         # # with c2:
#         #     with st.popover("Cost"):
#         #         st.markdown("some text here")
#         #     #st.button("Population", key = "five")
#         # with c3:
#         #     #with st.popover("Forest Area"):
#         #         #st.markdown("some text here")
#         #     #st.button("Forest Area", key = "six")
#         #     st.write()
#         # with c4:
#         #     with st.popover("Sustainable Removal Practices"):
#         #         st.markdown("some text here")
#         # with c5:
#         #     with st.popover("Crop Yield"):
#         #         st.markdown("some text here")
#         #     with st.popover("Cropland"):
#         #         st.markdown("a description")
#         #     with st.popover("Land Availability"):
#         #         st.markdown("description")
#         #     with st.popover("Extreme Weather"):
#         #         st.markdown("description")
#         #     with st.popover("Climate Change"):
#         #         st.markdown("description")
#         with c6:
#             #with st.popover("smth"):
#                 #st.markdown("some text here")
#                 st.write()

# with st.container(border=True):
#     left, right = st.columns([2,6])

#     with left:
#         st.markdown("Livestock Residues")
#     with right:
#         c1, c2, c3, c4, c5, c6 = st.columns(6)
        # with c1:
        #     #with st.popover("Crop Yield"):
        #         #st.markdown("some words here")
        #     #st.button("Crop Yield", key = "seven")
        #     st.write()
        # with c2:
        #     #with st.popover("Population"):
        #         #st.markdown("some text here")
        #     #st.button("Population", key = "eight")
        #     st.write()
        # with c3:
        #     with st.popover("Livestock Population"):
        #         st.markdown("some text here")
        #     #st.button("Forest Area", key = "nine")
        # with c4:
            #with st.popover("smth"):
                #st.markdown("some text here")
                # st.write()
        # with c5:
        #     #with st.popover("smth"):
        #         #st.markdown("some text here")
        #         st.write()
        # with c6:
        #     #with st.popover("smth"):
        #         #st.markdown("some text here")
        #         st.write()



# st.markdown("---")
# st.subheader("Driver Information")

# with st.container(border = True):
#     if st.session_state.selected_driver is None:
#         st.info("Click on a driver above to view its information.")
#     elif st.session_state.selected_driver == "Crop Yield":
#         st.subheader("Crop Yield")
#         st.caption("Type: Environmental")
#         st.write("Crop yield is influenced by ___")


