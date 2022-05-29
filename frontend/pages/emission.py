from cProfile import label
from enum import auto
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly as px
from streamlit_multipage import MultiPage
import plotly.figure_factory as ff

# from pages import app, customer, emission

# app = MultiPage()

# Add all your applications (pages) here
# app.add_page("Upload Data", app.app)
# app.add_page("Change Metadata", customer.app)
# app.add_page("Machine Learning", emission.app)
def app():
    st.title("Car Emission")

    auto_data = pd.read_csv("database/Car_Emission_Data_Clean.csv")
    
    st.subheader("Indian Vehicle Market")
    st.caption("Indian vehicle market is one of the biggest vehicle market in the world. We have taken a dataset which contains the following companies.")
    labels_home = auto_data['Make'].value_counts().to_dict().keys()
    sizes_home = auto_data['Make'].value_counts().to_dict().values()
    
    fig_home, ax_home = plt.subplots(figsize=(3, 3))
    ax_home.pie(sizes_home, labels=labels_home, autopct='%1.1f%%',
                shadow=True, startangle=90)
    ax_home.axis('equal') 
    st.pyplot(fig_home)
    
    st.subheader("Company and their Fuel Preferences")
    st.caption("The below scatterplot shows the different fuel types of the various cars these Indian companies manufacture")

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(
        auto_data["Fuel_Type"],
        auto_data["Make"],
    )

    ax.set_ylabel("Company Name")
    ax.set_xlabel("Fuel Type")
    st.write(fig)


        
    st.subheader("Fuel Tank Capacity and Displacement")
    st.caption("This scatterplot showing the relation between the fuel tank capacity and the displacement of the vehicle shows that they vary linearly.")
   
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(
        auto_data["Fuel_Tank_Capacity"],
        auto_data["Displacement"],
    )

    ax.set_ylabel("Displacment")
    ax.set_xlabel("Fuel Tank Capacity")
    st.write(fig)
    
    st.subheader("Kerb Weight")
    st.caption(f"The Kerb Weight distribution of the vehicles shows the variation of the kerb weights. Statistically, the maximum kerb weight is {auto_data['Kerb_Weight'].max()} kgs and the minumum kerb weight is {auto_data['Kerb_Weight'].min()} kgs")
    st.line_chart(auto_data['Kerb_Weight'])
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    st.subheader("Fuel Type and Kerb Weight")
    st.caption("The kerb weight variation of the vehicle with repect to the fuel type is shown in the scatterplot below. It is clear that the average kerb weight of petrol and diesel vehicles is comparable and the lowest average kerb weight being of the CNG fuel type vehicles")

    ax.scatter(
        auto_data["Fuel_Type"],
        auto_data["Kerb_Weight"],
    )

    ax.set_ylabel("Kerb Weight")
    ax.set_xlabel("Fuel Type ")
    st.write(fig)