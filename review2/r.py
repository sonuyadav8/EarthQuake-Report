import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Earthquake Data with missing values
data = {
    "Date": ["2023-01-02", "2023-02-15", "2023-03-01", "2023-04-12", "2023-05-05", 
             "2023-06-17", "2023-07-23", "2023-08-29"],
    "Latitude": [38.322, 36.121, 34.201, None, 35.689, 35.652, 37.774, -33.448],
    "Longitude": [-118.443, -117.865, -116.491, -72.434, 139.692, 140.084, -122.419, -70.669],
    "Magnitude": [5.2, None, 4.9, 6.1, 5.8, 6.0, 5.0, 5.6],
    "Depth_km": [7.0, 9.8, None, 10.0, 40.0, 45.0, 12.0, 35.0],
    "Location": ["Nevada, USA", "California, USA", "California, USA", "Haiti",
                 "Tokyo, Japan", "Chiba, Japan", "San Francisco, USA", "Santiago, Chile"]
}

# Load into a DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Summary before cleaning
print("Before Cleaning:\n", df.isnull().sum())

# Fill missing numerical data with mean
df['Magnitude'].fillna(df['Magnitude'].mean(), inplace=True)
df['Depth_km'].fillna(df['Depth_km'].mean(), inplace=True)
df['Latitude'].fillna(df['Latitude'].mean(), inplace=True)

# Summary after cleaning
print("\nAfter Cleaning:\n", df.isnull().sum())

# ---------------------------------
# VISUALIZATION SECTION BASED ON RUBRIC
# ---------------------------------

# Plot 1: Monthly Earthquake Count (Bar Chart)
monthly_counts = df['Date'].dt.to_period('M').value_counts().sort_index()
plt.figure(figsize=(10, 4))
monthly_counts.plot(kind='bar', color='skyblue')
plt.title("Monthly Earthquake Count")
plt.ylabel("Number of Earthquakes")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Magnitude Distribution (Histogram with KDE)
plt.figure(figsize=(6, 4))
sns.histplot(df['Magnitude'], bins=6, kde=True, color='salmon')
plt.title("Magnitude Distribution")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Plot 3: Depth vs Magnitude (Scatter Plot)
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='Depth_km', y='Magnitude', hue='Location', palette='Set2')
plt.title("Depth vs Magnitude by Location")
plt.xlabel("Depth (km)")
plt.ylabel("Magnitude")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Optional Interactive: Tooltip/Zoom - Use Plotly (if desired, not in this static version)

# DATA STORYTELLING NOTE:
# - Monthly frequency chart highlights temporal distribution
# - Magnitude histogram shows most quakes between 5.0 and 6.0
# - Depth vs Magnitude chart reveals no strong correlation, but regional variation is visible
