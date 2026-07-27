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

#create pestel tabs
political, economic, social, tech, environmental, legal = st.tabs(["Political", "Economic", "Social", "Technological", "Environmental", "Legal"])

with legal:
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

    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Urban Waste")
           
with environmental:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
        with right:
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                with st.popover("Afforestation"):
                    st.subheader("Afforestation")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                is ___ and __ and influenced by _______.           
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                _______ directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c2:
                with st.popover("Deforestation"):
                    st.subheader("Deforestation")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                is ___ and __ and influenced by _______.           
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                _____ directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c3:
                with st.popover("Land Availability"):
                    st.subheader("Land Availability")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                is ___ and __ and influenced by _______.           
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                _____ directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c4:
                with st.popover("Forest Fire"):
                    st.subheader("Forest Fire")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                is ___ and __ and influenced by _______.           
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                Higher crop yields directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c5:
                with st.popover("Disease"):
                    st.subheader("Disease")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                is ___ and __ and influenced by _______.           
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                Higher crop yields directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
                    
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
        with right:
            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                with st.popover("Crop Yield"):
                    st.subheader("Crop Yield")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
             is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
            with c2:
                with st.popover("Cropland"):
                    st.subheader("Cropland")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
             is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
            with c3:
                with st.popover("Land Availability"):
                    st.subheader("Land Availability")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
             is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
            with c4:
                with st.popover("Extreme Weather"):
                    st.subheader("Extreme Weather")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
             is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
            with c5:
                with st.popover("Climate Change"):
                    st.subheader("Climate Change")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
             is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                    st.divider()
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residues")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Urban Waste")
            
with tech:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
        with right:
                # c1 = st.columns(1)
                # with c1:
            with st.popover("Farming Practices/Equipment"):
                st.subheader("Farming Practices/Equipment")
                st.caption("Type: Technological")
                st.divider()
                st.markdown("""
            Crop yield is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
        with right:
            with st.popover("Sustainable Removal Practices"):
                st.subheader("Sustainable Removal Practices")
                st.caption("Type: Technological")
                st.divider()
                st.markdown("""
             is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Urban Waste")

with social:
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
                st.subheader("Livestock Population")
                st.caption("Type: Social")
                st.divider()
                st.markdown("""
            Livestock population is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of biomass produced.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Urban Waste")
        with right:
            with st.popover("City/Town Population"):
                st.subheader("City/Town Population")
                st.caption("Type: Social")
                st.divider()
                st.markdown("""
            Livestock population is ___ and __ and influenced by _______.           
                                            
            **As a Driver of Biomass Potential and Bioconversion:**
                            
            Higher crop yields directly increase the amount of biomass produced.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                                            
            insert links here """)

with economic:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
        with right:
            with st.popover("Cost"):
                st.subheader("Cost")
                st.caption("Type: Economic")
                st.divider()
                st.markdown("""
            Cost is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher costs ____ the amount of biomass produced.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
        with right:
            with st.popover("Cost"):
                st.subheader("Cost")
                st.caption("Type: Economic")
                st.divider()
                st.markdown("""
            Cost is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher costs ____ the amount of biomass produced.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
        with right:
            with st.popover("Cost"):
                st.subheader("Cost")
                st.caption("Type: Economic")
                st.divider()
                st.markdown("""
            Cost is ___ and __ and influenced by _______.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher costs ____ the amount of biomass produced.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Urban Waste")
                
with political:
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Forestry Biomass and Residues")
        with right:
            with st.popover("Canadian Policy"):
                st.subheader("Canadian Policy")
                st.caption("Type: Political")
                st.divider()
                st.markdown("""
            Canadian Policy involves the various regulations and laws put into place by the Canadian Government in regards to environmental issues, climate change and sustainability regulations. Policies such as the Net Zero Emissions goal can impact the funding and resources allocated towards biomass resources.           
                                    
            **As a Driver of Biomass Potential and Bioconversion:**
                    
            An increase in governmental policies supporting the use of biomass and renewable energy sources allows for an increase in funding towards the collection and useage of biomass as an energy resource, increasing the amount produced and collected.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                                    
            insert links here """)
                
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Agricultural Biomass and Residues")
        with right:
            with st.popover("Canadian Policy"):
                st.subheader("Canadian Policy")
                st.caption("Type: Political")
                st.divider()
                st.markdown("""
            Canadian Policy involves the various regulations and laws put into place by the Canadian Government in regards to environmental issues, climate change and sustainability regulations. Policies such as the Net Zero Emissions goal can impact the funding and resources allocated towards biomass resources.           
                                            
            **As a Driver of Biomass Potential and Bioconversion:**
                            
            An increase in governmental policies supporting the use of biomass and renewable energy sources allows for an increase in funding towards the collection and useage of biomass as an energy resource, increasing the amount produced and collected.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                                            
            insert links here """)
            
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Livestock Residue")
        with right:
            with st.popover("Canadian Policy"):
                st.subheader("Canadian Policy")
                st.caption("Type: Political")
                st.divider()
                st.markdown("""
            Canadian Policy involves the various regulations and laws put into place by the Canadian Government in regards to environmental issues, climate change and sustainability regulations. Policies such as the Net Zero Emissions goal can impact the funding and resources allocated towards biomass resources.           
                                            
            **As a Driver of Biomass Potential and Bioconversion:**
                            
            An increase in governmental policies supporting the use of biomass and renewable energy sources allows for an increase in funding towards the collection and useage of biomass as an energy resource, increasing the amount produced and collected.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                                            
            insert links here """)
    with st.container(border=True):
        left, right = st.columns([2,6])
        with left:
            st.markdown("Urban Waste")
        with right:
            with st.popover("Canadian Policy"):
                st.subheader("Canadian Policy")
                st.caption("Type: Political")
                st.divider()
                st.markdown("""
            Canadian Policy involves the various regulations and laws put into place by the Canadian Government in regards to environmental issues, climate change and sustainability regulations. Policies such as the Net Zero Emissions goal can impact the funding and resources allocated towards biomass resources.           
                                            
            **As a Driver of Biomass Potential and Bioconversion:**
                            
            An increase in governmental policies supporting the use of biomass and renewable energy sources allows for an increase in funding towards the collection and useage of biomass as an energy resource, increasing the amount produced and collected.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                                            
            insert links here """)

