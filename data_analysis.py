import pandas as pd
import folium
import folium.plugins

# Specify the file path
file_path = "D:\python\sfcrime_data\Police_Department_Incident_Reports__2018_to_Present_20240223.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the year 2024 data
# df = df[df['Incident Year'] == 2024]

# Create a folium map centered around San Francisco
sf_map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Add the heatmap layer to the map
heat_data = [[row['Latitude'], row['Longitude']] for index, row in df.iterrows()]

# if heat_data contains nan, remove it
heat_data = [x for x in heat_data if str(x[0]) != 'nan' and str(x[1]) != 'nan']

folium.plugins.HeatMap(heat_data).add_to(sf_map)

# Display the map
sf_map.save('heatmap_map.html')  # Save the map as an HTML file