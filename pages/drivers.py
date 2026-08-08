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
            Cropland consists of the amount of land allocated for purpose grown energy crops. Cropland can increase if more resources are allocated towards the agricultural industry, and it can be decreased if governmental spending shifts away from agriculture and the land is reallocated for industrial or commercial use. Cropland can also see decreases if extreme weather conditions render the soil infertile.          
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            More cropland directly increase the amount of agricultural biomass produced as there is a larger space to grow crops.""")
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
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
            with c4:
                with st.popover("Extreme Weather"):
                    st.subheader("Extreme Weather")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
            Extreme weather phenomena have seen an increase in frequency as the effects of climate change grow stronger. Extreme weather includes droughts, floods, heatwaves ad storms. All of these negatively impact the healthy growth of crops and damage cropland.
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Extreme weather phenomena can damage cropland as well as reduce the healthy crop harvest, decreasing the amount of agricultural biomass and residues available.""")
                    st.markdown("""              
            **Explore further literature**
                            
            insert links here """)
            with c5:
                with st.popover("Climate Change"):
                    st.subheader("Climate Change")
                    st.caption("Type: Environmental")
                    st.divider()
                    st.markdown("""
            Climate change is a long term shift in weather patterns globally, commonly causing an increase in temperatures and extreme weather. It is mainly caused by greenhouse gas emmissions from vehicles and agricultural systems into the atmosphere. Climate change raises temperatures, often resulting in longer periods of warm weather which allows for an increase in crop growing seasons. While this may allow for longer harvesting seasons, it also increases the chances of extreme weather that damages crops and cropland.             
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Despite having a small beneficial impact on crop harvesting and growing seasons, climate change increases frequency of extreme weather, causing a greater risk to crops and cropland. This can result in a decrease in harvestable agricultural biomass and residues.""")
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
            with st.popover("Harvesting Equipment"):
                st.subheader("Harvesting Equipment")
                st.caption("Type: Technological")
                st.divider()
                st.markdown("""
            As harvesting equiptment sees improvements in efficiency and a decrease in costs, more forestry biomass is able to be harvested. It also allows for a greater output when harvesting, allowing for more of the residues to be harvested and decreasing the amount left on the field. It is to be noted that this improvement is still restricted by the sustainable guidelines surrounding forestry residue harvesting.            
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            Improvements on harvesting equipment increase the amount of forestry biomasses collected efficiently and decrease costs surrounding harvesting, promoting the use of forestry residues as an energy source.""")
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
            Sustainable removal guidelines restrict the amount of agricultural biomass residues that are harvested from cropland. These guidelines ensure that enough residue is left on the land to preserve soil fertility and allow for future crops to succeed on the land.         
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            As sustainable removal guidelines are improved and increased, the amount of agricultural residues harvested significantly decreases.""")
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
            Livestock population consists of the number of livestock living on farms within the province. Its numbers are affected by birth and death rates, disease and weather. Disease and poor weather can result in higher death rates and significantly impact the healthy livestock population.           
                            
            **As a Driver of Biomass Potential and Bioconversion:**
            
            A greater livestock population directly results in greater livestock residues produced and vice versa.""")
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
            The population of cities and towns is impacted by birth rates, death rates, immigration and emmigration. An increasing shift towards the rural lifestyle has lead to emmigration of people from cities into towns. As towns oftentimes have smaller waste processing systems, this increase in population does not necessarily result in an increase of urban waste biomass as many towns do not have the infrastructure to process large amounts of waste.           
                                            
            **As a Driver of Biomass Potential and Bioconversion:**
                            
            City population drives the amount of urban waste biomass produced, whereas an shift of population into towns can decrease the amount of biomass produced unless infrastructure can meet the excessive load.""")
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

