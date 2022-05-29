from enum import auto
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly as px
# from streamlit_multipage import MultiPage
import plotly.figure_factory as ff
import streamlit_multipage as multipage

from multipage import MultiPage
# import multipage

from pages import car, customer, emission, electric_vehicles, two_wheeler_analysis


app = MultiPage()

app.add_page("Data Analysis", car.app)
app.add_page("Customer Segmentation Analysis", customer.app)
app.add_page("Car Emission", emission.app)
app.add_page("Electric Vehicles", electric_vehicles.app)
app.add_page("2 Wheeler Vehicles", two_wheeler_analysis.app)

app.run()
