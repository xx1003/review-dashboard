import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Hello world from local PC")

tips = sns.load_dataset("tips")

fig, ax = plt.subplots(figsize=(10,6))

sns.barplot(data=tips, x='day', y='total_bill', ax=ax)
st.pyplot(fig)
