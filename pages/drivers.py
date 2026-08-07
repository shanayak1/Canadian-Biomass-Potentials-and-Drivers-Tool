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
                Forestry biomass and residues are greatly impacted by land availability. Afforestation increases the area of available forests, countering the effects of deforestation. As the current afforestation rate is significantly less than the previously low deforestation rate in Canada, this driver does not have a large contribution to the land availability.        
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                Afforestation directly impacts the amount of available land for forestry use, therefore, an increase in Afforestation will cause a slight increase in forestry biomass as the amount of available land to grow and collect forestry biomass increases.""")
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c2:
                with st.popover("Deforestation"):
                    st.subheader("Deforestation")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                Forestry biomass and residues are greatly impacted by land availability. Deforestation decreases the area of available forests, countering the effects of afforestation. Deforestation rates in Canada are relatively low compared to most countries in the world, however the reallocation of forestry land for commercial and industrial use has increased as the demand on Canadian infrastructure increases.          
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                Deforestation directly impacts the amount of available land for forestry use, therefore, an increase in deforestation will cause a decrease in forestry biomass as the amount of available land to grow and collect forestry biomass decreases.""")
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c3:
                with st.popover("Land Availability"):
                    st.subheader("Land Availability")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                Land availability consists of the land that is allocated by the government for forestry uses. Deforestation and afforestation both affect this driver. The largest causes of change in land availability for forestry are changes in policy reallocating land towards industrial or commercial uses. Canadian policy regarding the conservation of national and provincial parks also decreases the amount of land available for forestry harvesting.           
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                Land availability directly correlates with the amount of forestry biomass produced. When more land is allocated towards forestry use, more forestry biomass is produced and consequentally, more forestry residues are produced. """)
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c4:
                with st.popover("Forest Fire"):
                    st.subheader("Forest Fire")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                Forest fires decrease the amount of available forestry residues and decimate current forestry biomass supply. They often limit the amount of harvestable timber. Forest fire frequency has increased significantly over the past decade as climate change brings more severe weather, including excessive heat waves and drought.          
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                As forest fires are known to decrease the available timber supply and forestry residues, they directly decrease the amount of forestry biomass and forestry residues available for use. The consistant increase in wildfires proves that this is an important driver of forestry biomass and residue supply.""")
                    st.markdown("""              
                **Explore further literature**
                                
                insert links here """)
            with c5:
                with st.popover("Disease"):
                    st.subheader("Disease")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
                Disease is common among forests in Alberta and British Columbia. Around 4.6 million hectares are affected by disease in British Columbia annually and approximately 0.5 million hectares are impacted by diesease in Alberta. Out of Alberta and British Columbia's total available forestry land of 38 and 60.3 million hectares respectively, this number may seem insignificant, however, forest pests and disease spread fast and leave no harvestable biomass or biomass residues. These diseases not only limit the current biomass supply, but continue to decrease the supply for years to come as forests require intensive time to recover.          
                                
                **As a Driver of Biomass Potential and Bioconversion:**
                
                Disease and pests directly decrease the amount of available forestry land. If forest dieases are mitigated, forest health can be preserved.""")
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
            Crop yield is measured by the amount of crops harvested off of agricultural land annually. Crop yields are influenced by a variety of factors, including weather conditions, soil quality, irrigation practices, crop health and disease. The size of cropland available also influences the crop yield. Climate change plays a large role in determining crop yield as extreme weather conditions such as droughts, floods and heatwaves can damage fields and crops, harming present and future yield. Crop yield is a pertinent factor in the agricultural biomass category.          
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Higher crop yields directly increase the amount of agricultural biomass and residues produced.""")
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
            with c2:
                with st.popover("Cropland"):
                    st.subheader("Cropland")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
            .           
                            
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
            Land availability consists of the land that is allocated by the government for forestry uses. Deforestation and afforestation both affect this driver. The largest causes of change in land availability for forestry are changes in policy reallocating land towards industrial or commercial uses. Canadian policy regarding the conservation of national and provincial parks also decreases the amount of land available for forestry harvesting.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Land availability directly correlates with the amount of agricultural biomass produced. When more land is allocated towards agricultural use, more agricultural biomass is produced and consequentally, more agricultural residues are produced.""")
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
                st.markdown("""Canadian Policy involves the various regulations and laws put into place by the Canadian Government in regards to environmental issues, climate change and sustainability regulations. Policies such as the Net Zero Emissions goal can impact the funding and resources allocated towards biomass resources.           
                                            
            **As a Driver of Biomass Potential and Bioconversion:**
                            
            An increase in governmental policies supporting the use of biomass and renewable energy sources allows for an increase in funding towards the collection and useage of biomass as an energy resource, increasing the amount produced and collected.""")
                st.divider()
                st.markdown("""              
            **Explore further literature**
                                            
            insert links here """)

