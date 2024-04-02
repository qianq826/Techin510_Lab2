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


df_filtered = df[(df['species'].isin(species)) & (df['island'].isin(island)) & (df['sex'].isin(sex))]


st.write(df_filtered)


# Visualization 1: Scatter Plot comparing flipper length and body mass
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df_filtered, x='flipper_length_mm', y='body_mass_g', hue='species', style='sex', ax=ax1)
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Flipper Length vs. Body Mass by Species and Sex')
st.pyplot(fig1)

# Visualization 2: Histogram for bill length
fig2, ax2 = plt.subplots()
sns.histplot(df_filtered['bill_length_mm'], kde=True, color='skyblue', ax=ax2)
plt.xlabel('Bill Length (mm)')
plt.ylabel('Frequency')
plt.title('Distribution of Bill Length')
st.pyplot(fig2)
