import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🐧 Penguins Explorer")
st.write("Welcome to the Penguins Explorer! This app allows you to explore the Palmer Penguins dataset. Use the widgets to filter data and view different visualizations.")

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

# Clean data - drop rows with missing values
df.dropna(inplace=True)

# Sidebar filters
species = st.sidebar.multiselect('Select Species', options=df['species'].unique(), default=df['species'].unique())
island = st.sidebar.multiselect('Select Island', options=df['island'].unique(), default=df['island'].unique())
sex = st.sidebar.multiselect('Select Sex', options=df['sex'].unique(), default=df['sex'].unique())

# Filtering data based on selection
df_filtered = df[(df['species'].isin(species)) & (df['island'].isin(island)) & (df['sex'].isin(sex))]

# Display filtered data
st.write(df_filtered)

# Visualization (using seaborn and matplotlib)
fig, ax = plt.subplots()
sns.histplot(df_filtered['flipper_length_mm'], kde=True, ax=ax)
st.pyplot(fig)