import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Data Analysis In The Field of Automotive Industry")
st.subheader("Are you planning to launch a new vehicle or open your own automobile venture? Renowned automobile industries are using the power of data analytics to improvise their sales, make informed decisions and take customer's concern and needs into account")
st.write("Every automobile maker releases various models, checkout some of the renowned ones")

# auto_data = pd.read_csv("Car_Features_Dataset.csv")
auto_data = pd.read_csv("cars_engage_2022.csv")