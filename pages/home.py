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

st.subheader("Biomass Classifications")
st.text("Within the Canadian Biomass landscape, biomass can be classified into six categories in accordance with Canadian Standards. Canadian Standards for biomass categories classify the different biomass types by origin which is a similar classification method as that used by the International Standards.")

cats_df = pd.DataFrame({
    "Term": [
        "Forestry Biomass",
        "Forestry Residue",
        "Purpose Grown Energy Crops",
        "Crop Residue",
        "Livestock Residue",
        "Urban Waste",
    ],
    "Definition":[
        "Forestry Biomass consists of the biomass produced through the forestry industry, including fuelwood, firewood and lumber",
        "Forestry Residue includes the unused materials from trees after the harvesting and processing stages of making lumber or any non-energy uses within the Forestry industry.",
        "Purpose grown energy crops are inclusive of any crops that are grown for energy, such as wheat, canola and switchgrass.",
        "Crop Residue is defined as the remains of plants after the crops are harvested and processed. This includes the residue of wheat, canola, soybean, barley and flaxseeds.",
        "Livestock residue consists of the remains, such as manure, procduced by livestock such as cows and horses.",
        "Urban waste includes waste from residents and other commercial activities. This includes, but is not limited to wastewater, biosolids, source separated organics and pulp mill sludge.",
    ]
})

with st.container():
    st.table(cats_df)

st.subheader("References")
st.text("The following references were used in the formulation and research behind this Biomass Tool:")

references = """
[1] “Livestock statistics | Alberta.ca.” Accessed: Jul. 09, 2026. [Online]. Available: https://www.alberta.ca/livestock-statistics

[2] “Business, industry and trade statistics | Alberta.ca.” Accessed: May 09, 2026. [Online]. Available: https://www.alberta.ca/business-industry-and-trade-statistics

[3] “July 1, 2024 Livestock Inventory Estimates,” 2024.

[4] “Carbon capture and storage technologies: present scenario and drivers of innovation,” Current Opinion in Chemical Engineering, vol. 17, pp. 22–34, Aug. 2017, doi: 10.1016/j.coche.2017.05.004.

[5] “A review of agricultural crop residue supply in Canada for cellulosic ethanol production,” Renewable and Sustainable Energy Reviews, vol. 16, no. 5, pp. 2954–2965, Jun. 2012, doi: 10.1016/j.rser.2012.02.013.

[6] “University of Calgary Libraries & Cultural Resources | University of Calgary Library,” Libraries & Cultural Resources | University of Calgary. Accessed: May 09, 2026. [Online]. Available: http://library.ucalgary.ca/

[7] “The State of Canada’s Forests: Annual Report 2025 - Natural Resources Canada.” Accessed: Jul. 08, 2026. [Online]. Available: https://natural-resources.canada.ca/forests-forestry/state-canada-forests/state-canada-s-forests-annual-report-2025#_Indicator_:_Forest

[8] “Systems Dynamics - an overview | ScienceDirect Topics.” Accessed: Jun. 28, 2026. [Online]. Available: https://www.sciencedirect.com/topics/engineering/systems-dynamics

[9] “Natural Resources Canada.” Accessed: Jul. 08, 2026. [Online]. Available: https://natural-resources.canada.ca/

[10] “Lumber production, shipments, and stocks by species, monthly.” Accessed: Jul. 09, 2026. [Online]. Available: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1610001701&pickMembers%5B0%5D=1.10&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2024&cubeTimeFrame.endMonth=12&cubeTimeFrame.endYear=2024&referencePeriods=20240101%2C20241201

[11] “Feedstock,” CAPP | A Unified Voice for Canada’s Upstream Oil and Gas Industry. Accessed: May 09, 2026. [Online]. Available: https://www.capp.ca/en/glossary/feedstock/

[12] “Fast Stats 2020 British Columbia’s Agriculture, Food and Seafood Sector”.

[13] “Factsheets for biobased CO2 removal options in Germany”.

[14] “Characterization of Canadian biomass for alternative renewable biofuel - ScienceDirect.” Accessed: May 09, 2026. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0960148109003838?casa_token=Y4Ay5169KAwAAAAA:9jB7kM_ykVIXgZJJ5Ar3XNLB5kPLxJaOEvQZIoaM67c16cxXLAFC5lBwASB_vQ5teQ7ms9gA_Q

[15] “Carbon Content - an overview | ScienceDirect Topics.” Accessed: May 27, 2026. [Online]. Available: https://www.sciencedirect.com/topics/computer-science/carbon-content

[16] “Biomass potential | Knowledge for policy.” Accessed: May 27, 2026. [Online]. Available: https://knowledge4policy.ec.europa.eu/glossary-item/biomass-potential_en

[17] “Biomass Energy - an overview | ScienceDirect Topics.” Accessed: Aug. 24, 2026. [Online]. Available: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/biomass-energy

[18] “Biomass Energy - an overview | ScienceDirect Topics.” Accessed: Aug. 24, 2026. [Online]. Available: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/biomass-energy

[19] “Biomass characteristics – European Biomass Industry Association.” Accessed: May 08, 2026. [Online]. Available: https://www.eubia.org/cms/wiki-biomass/biomass-characteristics-2/

[20] “Bio-economy Facts,” BioTalent Canada. Accessed: May 09, 2026. [Online]. Available: https://www.biotalent.ca/bio-economy-facts/

[21] “Alberta’s Forest Economy 2023”.

[22] “Agriculture Facts”.

[23] “21-021-MIE - Appendix - Manure production (as excreted) coefficients, Canada, 2001.” Accessed: Jul. 09, 2026. [Online]. Available: https://www150.statcan.gc.ca/n1/pub/21-021-m/2004001/t/4144625-eng.htm?

[24] H. H. Welling and T. J. Shaw, “Energy From Wood Biomass Combustion In Rural Alberta Applications”.

[25] Vizzuality, “Alberta, Canada Deforestation Rates & Statistics | GFW.” Accessed: Jul. 08, 2026. [Online]. Available: https://www.globalforestwatch.org/dashboards/country/CAN/1?category=undefined

[26] B. D. Titus et al., “Sustainable forest biomass: a review of current residue harvesting guidelines,” Energ Sustain Soc, vol. 11, no. 1, p. 10, Apr. 2021, doi: 10.1186/s13705-021-00281-w.

[27] Statistics Canada, “Lumber production, shipments, and stocks by species, monthly.” Government of Canada. doi: 10.25318/1610001701-ENG.

[28] S. Richter, N. Szarka, A. Bezama, and D. Thrän, “What Drives a Future German Bioeconomy? A Narrative and STEEPLE Analysis for Explorative Characterisation of Scenario Drivers,” Sustainability, vol. 14, no. 5, p. 3045, Jan. 2022, doi: 10.3390/su14053045.

[29] G. Reznowski, “LibGuides: Industry Research: PESTEL Analysis.” Accessed: Jun. 21, 2026. [Online]. Available: https://libguides.libraries.wsu.edu/c.php?g=294263&p=4358409

[30] X. Li, E. Mupondwa, S. Panigrahi, L. Tabil, S. Sokhansanj, and M. Stumborg, “A review of agricultural crop residue supply in Canada for cellulosic ethanol production,” Renewable and Sustainable Energy Reviews, vol. 16, no. 5, pp. 2954–2965, Jun. 2012, doi: 10.1016/j.rser.2012.02.013.

[31] L. M. Jacob, K. N. Irvine, B. B. Beza, and L. H. C. Chua, “Adaptive resilience in wetlands: An integrative review of principles, research gaps, and ways forward for better adaptive management,” Ecological Engineering, vol. 220, p. 107720, Oct. 2025, doi: 10.1016/j.ecoleng.2025.107720.

[32] S. C. Government of Canada, “Wastewater volumes processed by municipal sewage systems.” Accessed: Jul. 09, 2026. [Online]. Available: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3810009901

[33] S. C. Government of Canada, “Lumber production, shipments, and stocks by species, monthly.” Accessed: Jun. 01, 2026. [Online]. Available: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1610001701

[34] S. C. Government of Canada, “British Columbia lumber production, monthly.” Accessed: Jul. 09, 2026. [Online]. Available: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1610001705

[35] C. E. R. Government of Canada, “CER – Market Snapshot: Canada’s Bioenergy Diversity and Potential.” Accessed: May 08, 2026. [Online]. Available: https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2023/market-snapshot-canada-bioenergy-diversity-potential.html

[36] N. R. Canada, “The State of Canada’s Forests: Annual Report 2025.” Accessed: Jul. 08, 2026. [Online]. Available: https://natural-resources.canada.ca/forests-forestry/state-canada-forests/state-canada-s-forests-annual-report-2025

[37] N. R. Canada, “Bioenergy systems.” Accessed: May 09, 2026. [Online]. Available: https://natural-resources.canada.ca/energy-sources/renewable-energy/bioenergy-systems

[38] N. R. Canada, “Domestic production.” Accessed: Jul. 09, 2026. [Online]. Available: https://cfs.cloud.nrcan.gc.ca/statsprofile/investment/domestic-production.html

[39] A. and A.-F. Canada, “Canada: Outlook for Principal Field Crops, 2026-05-21.” Accessed: Jul. 09, 2026. [Online]. Available: https://agriculture.canada.ca/en/sector/crops/reports-statistics/canada-outlook-principal-field-crops-2026-05-21

[40] B. Boundy and S. C. Davis, “Biomass Energy Data Book: Edition 3”.

"""
st.markdown(references)