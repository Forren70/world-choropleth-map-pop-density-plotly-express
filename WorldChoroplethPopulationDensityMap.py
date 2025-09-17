import os
import pandas as pd
import plotly.express as px
import numpy as np

# Relative path to the CSV file (in the same folder as the script)
file_path = os.path.join(os.path.dirname(__file__), "population_density_per_square_km_2025.csv")

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"CSV file not found: {file_path}")

# Load the CSV
df = pd.read_csv(file_path, sep=';', quotechar='"')

# Rename the column and create a log-scaled version
df.rename(columns={'2025': 'density'}, inplace=True)
df['Log-scaled Population Density'] = np.log10(df['density'] + 1)  # avoid log(0)

# Create custom hover text
df['custom_hover'] = df.apply(
    lambda row: f"<b>{row['country']}</b><br>"
                f"Density: {row['density']:,} per km²<br>"
                f"Log Density: {row['Log-scaled Population Density']:.2f}",
    axis=1
)

# Create the choropleth map
fig = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='Log-scaled Population Density',
    hover_name='country',
    hover_data={'Log-scaled Population Density': False, 'custom_hover': True},
    color_continuous_scale=[
        [0.0, 'rgb(255, 255, 153)'],   # yellow for low density
        [0.5, 'rgb(102, 204, 102)'],   # green for medium density
        [1.0, 'rgb(0, 0, 204)']        # blue for high density
    ],
    projection='natural earth',
    title='World Population Density (2025)'
)

# Use hovertemplate to show custom hover text
fig.update_traces(hovertemplate=df['custom_hover'])

# Display the map
fig.show()

# Save the map as an HTML file
fig.write_html("Population_density_map_by_country.html")


