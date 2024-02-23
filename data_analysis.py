import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = "D:\python\sfcrime_data\Police_Department_Incident_Reports__2018_to_Present_20240223.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Create a scatter plot using Latitude and Longitude as x and y
plt.scatter(df['Latitude'], df['Longitude'])
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Scatter Plot of Data Points')
plt.show()
