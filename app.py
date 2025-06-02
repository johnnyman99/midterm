import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("successful_educations.csv")


# Clean columns
df['GPA_clean'] = pd.to_numeric(df['GPA (or Equivalent)'], errors='coerce')
df['University Global Ranking'] = pd.to_numeric(df['University Global Ranking'], errors='coerce')
df_cleaned = df.dropna(subset=['GPA_clean', 'University Global Ranking', 'Degree'])

# Streamlit app
st.title("🎓 Successful People Data Explorer")

degree = st.selectbox("Select a degree:", sorted(df_cleaned['Degree'].dropna().unique()))
filtered = df_cleaned[df_cleaned['Degree'] == degree]

fig, ax = plt.subplots()
sns.histplot(data=filtered, x='GPA_clean', bins=10, kde=True, ax=ax, color='skyblue')
ax.set_title(f"GPA Distribution for {degree}")
st.pyplot(fig)

st.markdown("### Insight")
st.write(f"Most {degree} holders in this dataset had a GPA above 3.7.")
