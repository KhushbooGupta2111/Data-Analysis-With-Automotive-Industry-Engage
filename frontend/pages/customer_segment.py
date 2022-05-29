import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly as px

import plotly.figure_factory as ff

def app():
    st.title("Customer Segment Analysis")
    with st.sidebar:
        selected = option_menu(
            menu_title="Autolysis" ,
            options=["Four Wheeler", "Two Wheeler" , "Potential customers" , "Electric Vehicles", "Safety Norms"],
        )

    st.title("Customer Segmentation Analysis")

    auto_data = pd.read_csv('database/Customer Segment Data.csv')
    makes = (auto_data["Car Type"].value_counts()).to_frame();
    st.bar_chart(makes)

    auto_data.set_index("Car Type", inplace = True)



    st.subheader("House Loan")
    labels = auto_data['House Loan'].value_counts().to_dict().keys()
    sizes = auto_data['House Loan'].value_counts().to_dict().values()
        
        # explode = (0, 0.1, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
    ax1.axis('equal') 
    st.pyplot(fig1)

    st.subheader("Personal Loan")
    labels = auto_data['Personal loan'].value_counts().to_dict().keys()
    sizes = auto_data['Personal loan'].value_counts().to_dict().values()
        
        # explode = (0, 0.1, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
    ax1.axis('equal') 
    st.pyplot(fig1)

    st.subheader("Number of Dependents")
    labels = auto_data['No of Dependents'].value_counts().to_dict().keys()
    sizes = auto_data['No of Dependents'].value_counts().to_dict().values()
        

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
    ax1.axis('equal') 
    st.pyplot(fig1)

    # hist_values = np.histogram(
    #     auto_data['Age'].dt.hour, bins=24, range=(0,24))[0]
    # fig = px.density_heatmap(auto_data, x="Age", y="Price")
    # fig.show()

    # st.line_chart(auto_data["Total Salary"],auto_data["Wife Salary"],auto_data["Salary"])


    st.subheader("Salary vs Wife Salary")
    st.bar_chart(auto_data[["Salary" , "Wife Salary"]])
    # st.line_chart(auto_data["Age"])
    st.subheader("Age Chart")
    st.bar_chart(auto_data["Age"])

    # Age Pie Chart
    st.subheader("Age groups")
    labels = auto_data['Age'].value_counts().to_dict().keys()
    sizes = auto_data['Age'].value_counts().to_dict().values()
        
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
    ax1.axis('equal') 

    st.subheader("Age groups")
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)


    st.subheader("Scatter Plots for Wife Working")
    ax.scatter(
        auto_data["Wife Working"],
        auto_data["Price"],
    )

    ax.set_ylabel("Ex-Showroom Price")
    ax.set_xlabel("Wife Working")

    st.write(fig)

    st.subheader("Price vs Total Salay")
    st.bar_chart(auto_data[['Price' , 'Total Salary']])