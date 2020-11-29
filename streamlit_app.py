#adding necessary libraries

import streamlit as st
import pandas as pd
import lifetimes
import numpy as np
np.random.seed(42)
import altair as alt
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.markdown(""" # Customer Lifetime Prediction App 👋


Upload the RFM data and get your customer lifetime prediction on the fly !!! :smile:

	""")


st.image("https://sarasanalytics.com/wp-content/uploads/2019/11/Customer-Lifetime-value-new-1.jpg", use_column_width = True)


data = st.file_uploader("File Uploader")

st.sidebar.image("http://logok.org/wp-content/uploads/2014/06/City-of-Melbourne-logo-M.png", width = 120)
st.sidebar.markdown(""" **Made with :heart: by Mukul Singhal** """)


st.sidebar.title("Input Features :pencil:")


st.sidebar.markdown("""

[Example CSV Input File](https://raw.githubusercontent.com/mukulsinghal001/customer-lifetime-prediction-using-python/main/model_deployment/sample_file.csv)

	""")

days = st.sidebar.slider("Select The No. Of Days", min_value = 1, max_value = 365, step = 1, value = 30)

profit = st.sidebar.slider("Select the Profit Margin", min_value = 0.01, max_value = 0.09, step = 0.01, value = 0.05)
