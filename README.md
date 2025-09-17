# World Choropleth Map of Population Density (2025)

This repository contains a Python project that creates an **interactive world choropleth map** 
showing population density per square kilometer for the year 2025.

## Description

The script **`WorldChoroplethPopulationDensityMap.py`** uses **Plotly Express** 
to visualize population density data.  
It applies a logarithmic transformation to density values to improve color contrast on the map.  
When hovering over a country, the map shows both the actual density and the log-scaled value.

## Data

The project uses the following datasets:

- **Original datasets from Gapminder**:  
  - `population_density_per_square_km.csv`  
  - `population_density_per_square_km.xlsx`  
  These contain population density for all years, including 2025.

- **Filtered datasets used by the script**:  
  - `population_density_per_square_km_2025.csv`  
  - `population_density_per_square_km_2025.xlsx`  
  These files contain only the 2025 population density data 
  and are used directly by the script.

## Output

The script generates an **interactive choropleth map** and saves it as:

- `Population_density_map_by_country.html`

You can open this file in any web browser to explore population density 
visually across the world.  

Below is a snapshot of the map:

![World Population Density Map](Population_density_map_by_country.html)

## How to Use

1. Make sure all the required data files are in the same folder as the script.  
2. Run the script using Python (Python 3.8+ recommended).  
3. The interactive map will open automatically 
   and the HTML file will be saved in the same folder.

## Requirements

- Python 3.8 or higher  
- pandas  
- numpy  
- plotly
