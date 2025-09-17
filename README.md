# World Choropleth Map of Population Density (2025)

This repository contains a Python project that creates an **interactive world choropleth map** 
showing the **population density of each country** (people per square kilometer) for 2025.

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
  These were downloaded from [Gapminder Data](https://www.gapminder.org/data/) 
  using the search term **"population density (per square km)"**.  
  They contain population density for all countries and for all years, including 2025.

- **Modified datasets for 2025 used by the script**:  
  - `population_density_per_square_km_2025.csv`  
  - `population_density_per_square_km_2025.xlsx`  
  These files were created from the original Gapminder datasets by removing all 
  columns except two: the **country names** and the **population density for 2025**.  
  All data for previous years were deleted.

## Output

The script generates an **interactive choropleth map** and saves it as:

- `Population_density_map_by_country.html`

You can open this file in any web browser to explore the **population density of each country**.  

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
