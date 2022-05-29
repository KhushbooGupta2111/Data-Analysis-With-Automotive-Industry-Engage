from pyexpat import features
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from sqlalchemy import column
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


make = st.selectbox('Choose your company name' , auto_data["Make"].unique())
company_data = auto_data[['Model' , 'Variant' , 'Ex-Showroom_Price']].where(auto_data['Make'] == make).dropna();

# st.write(company_data)

model = st.selectbox('Choose your car name' , company_data["Model"].unique())
variant_data = company_data[['Variant' , 'Ex-Showroom_Price']].where(company_data['Model'] == model).dropna();

variant = st.selectbox('Choose your variant name' , variant_data['Variant'].unique())

# st.write(variant_data['Ex-Showroom_Price'].where(variant_data['Variant'] == variant))
price_data = variant_data['Ex-Showroom_Price'].where(variant_data['Variant'] == variant).dropna()

st.header("Car Price")
st.write(price_data)

st.text("")
specifications , features , safety = st.columns(3)
entertainment , exterior , interior = st.columns(3)

with specifications:
    specifications_button = st.button('Specifications')

with features:
    features_button = st.button('Features')

with safety:
    safety_button = st.button('Safety')

with entertainment:
    entertainment_button = st.button('Entertainment')

with exterior:
    exterior_button = st.button('Exterior')

with interior:
    interior_button = st.button('Interior')

    if specifications_button:
        st.title("Specifications")

    st.subheader("Car Dimentions")
    st.write(auto_data[['Length' , 'Width' , 'Height']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data[['Wheels_Size' , 'Ground_Clearance']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data[['Seating_Capacity' , 'Boot_Space']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data[['Front_Track' , 'Rear_Track']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

    st.subheader("Car Weight and Performace")
    st.write(auto_data[['Kerb_Weight' , 'Gross_Vehicle_Weight']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data['Minimum_Turning_Radius'].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

    st.subheader("Mileage")
    st.write(auto_data['City_Mileage'].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

    st.subheader("Engine Specifications")
    st.write(auto_data['Displacement'].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data[['Power' , 'Torque' , 'Cylinders']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

    st.subheader("Braking Specifications")
    st.write(auto_data[["Front_Brakes" , "Rear_Brakes"]].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

if features_button:
    st.title("Features")

    st.subheader("Airbags")

if safety_button:
    st.title("Safety")
    
    st.header("Airbags")
    st.write(auto_data[['Airbags' , 'Number_of_Airbags']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

    st.header("Warnings and Controls Systems")
    st.write(auto_data[['High_Speed_Alert_System' , 'ESP_(Electronic_Stability_Program)']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data[['Tyre_Pressure_Monitoring_System' , 'Engine_Malfunction_Light']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data[['Central_Locking' , 'Passenger_Side_Seat-Belt_Reminder']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

    st.header("Child Safety")
    st.write(auto_data[['Child_Safety_Locks' , 'ISOFIX_(Child-Seat_Mount)']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

    st.header("Brakings")
    st.write(auto_data[["Front_Brakes" , "Rear_Brakes"]].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())
    st.write(auto_data[['ABS_(Anti-lock_Braking_System)' , 'EBD_(Electronic_Brake-force_Distribution)' , 'EBA_(Electronic_Brake_Assist)']].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())

if entertainment_button:
    st.title("Audio and Entertainment")

if exterior_button:
    st.title("Exteriors")

if interior_button:
    st.title("Interiors")

# st.write(auto_data['Ground_Clearance'].where((auto_data['Make'] == make) & (auto_data['Model'] == model) & (auto_data['Variant'] == variant)).dropna())


# price = st.selectbox('Price of the car' , price_data.unique())
# st.write("Tata")
# st.table(pd.DataFrame(auto_data["Model"].where(auto_data["Make"] == "Tata").unique()).dropna())

# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .column_heading.level0 {display:none}
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

with st.sidebar:
   selected = option_menu(
       menu_title="Autolysis" ,
       options=["Four Wheeler", "Two Wheeler" , "Potential customers" , "Electric Vehicles", "Safety Norms"],
       orientation=HORIZONTAL
   )