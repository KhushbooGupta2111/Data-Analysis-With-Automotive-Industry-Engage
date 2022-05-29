import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from streamlit_multipage import MultiPage


def app():
    st.title("Two Wheeler Analysis")
    auto_data = pd.read_csv("Two Wheeler Data.csv")

    from datetime import date
    current_year = date.today().year

    auto_data['year'] = current_year - auto_data['year']
    auto_data.rename(columns = {'year':'bike_age'}, inplace = True)



    # Plotting
    st.subheader("Ownership Type")
    st.bar_chart(auto_data['owner'].value_counts())

    st.subheader("Ownership vs Selling Price")

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(
        auto_data["owner"],
        auto_data["selling_price"],
    )

    ax.set_ylabel("Ex-Showroom Price")
    ax.set_xlabel("Wife Working")

    st.write(fig)

    st.subheader("Bike Age vs Distance Driven")
    st.line_chart(auto_data[['km_driven' , 'bike_age']])

    auto_data.set_index('km_driven', inplace = True)
    st.subheader("KMs Driven vs Ex-Showroom Price")
    st.line_chart(auto_data['ex_showroom_price'])

    auto_data.set_index('bike_age', inplace = True)
    st.subheader("Pricing vs Bike Age")
    st.line_chart(auto_data[['ex_showroom_price' , 'selling_price']])

