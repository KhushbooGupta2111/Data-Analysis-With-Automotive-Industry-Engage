from pyexpat import features
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from sqlalchemy import column
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

st.title("Data Analysis In The Field of Automotive Industry")
st.subheader("Are you planning to launch a new vehicle or open your own automobile venture? Renowned automobile industries are using the power of data analytics to improvise their sales, make informed decisions and take customer's concern and needs into account")
st.write("Every automobile maker releases various models, checkout some of the renowned ones")

# auto_data = pd.read_csv("Car_Features_Dataset.csv")
auto_data = pd.read_csv("cars_engage_2022.csv")

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