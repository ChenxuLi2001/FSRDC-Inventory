# FSRDC-Inventory
**GitHub Pages Landing Page**: [Click here](https://chenxuli2001.github.io/FSRDC-Inventory/)
This project collects and visualizes research outputs from the FSRDC program.

## Project Goals
- Produce an inventory of research outputs resulting from FSRDC projects in an open format to include
common reference elements, metadata, and any associated persistent digital identifiers such as
DOIs for each entry in the inventory.
- Compile source code used in creating the index and gathering information.
- Create a GitHub Pages landing page to host a human-readable version of the inventory, statistics on the
inventory, any supporting graphics, and a comprehensive project summary written in a narrative
format.

## Project Structure
- `data/` - Contains collected research output data in JSON/CSV format.
- `codes/` - Python scripts for collecting and processing data.
- `docs/` - Documentation and resources.

## Code Descriptions
- `fetch_crossref.py` - Collect 500 related papers from Crossref API website.
- `fetch_google.py` - Collect 500 related papers from Google Scholar.
- `merge_data.py` - Merge the two generated datasets to get a more complete dataset containing papers from both sources. Duplicate papers are removed.
- `visualization.py` - Visualize the collected data for future analysis.

## How to Operate
1. Run the "codes/fetch_crossref.py" and "codes/fetch_google.py".
2. Run the "codes/merge_data.py" and generate the final dataset.
3. Using the final dataset, run "codes/visualization.py".
4. Store the generated result figures.

## License
This project is licensed under the MIT License.