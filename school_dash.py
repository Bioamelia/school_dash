import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "ACTTHS1.xlsx"  # Ensure this file is in the working directory
df = pd.read_excel(file_path, engine="openpyxl")

# Final Data Cleaning
df.replace({"--": None, " ": None, "": None}, inplace=True)
df = df.apply(pd.to_numeric, errors="coerce")
df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill missing values

# Select only relevant columns for correlation heatmap
important_columns = ["Composite", "Math Score", "Science Score", "English Score", "Reading Score"]
df_filtered = df[important_columns]  # Keep only ACT scores

# Sidebar filters
st.sidebar.header("Filters")
selected_subject = st.sidebar.selectbox("Select Score Category:", important_columns)

# Dashboard Title
st.title("📊 ACT Performance Dashboard")
st.write("This dashboard provides insights into ACT performance trends.")

# Summary statistics
st.subheader(f"Summary Statistics for {selected_subject}")
st.write(df[selected_subject].describe())

# Histogram of selected subject
st.subheader(f"Distribution of {selected_subject} Scores")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df[selected_subject], bins=30, kde=True, color="blue", ax=ax)
plt.xlabel("Score")
plt.ylabel("Frequency")
st.pyplot(fig)

# Box Plot of selected subject
st.subheader(f"Box Plot for {selected_subject}")
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(y=df[selected_subject], color="lightblue", ax=ax)
plt.ylabel("Score")
st.pyplot(fig)

# Correlation Heatmap (Filtered for Readability)
st.subheader("Correlation Between ACT Scores")
fig, ax = plt.subplots(figsize=(8, 6))  # Adjust figure size
sns.heatmap(df_filtered.corr(), annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Conclusion
st.write("This dashboard helps identify school-wide trends and areas for improvement.")
