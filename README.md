# FSRDC-Inventory
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

## How to Operate
1. Run the "codes/fetch_crossref.py" and "codes/fetch_google.py".
2. Run the "codes/merge_data.py" and generate the final dataset.
3. Using the final dataset, run "codes/visualization.py".
4. Store the generated result figures.

## License
This project is licensed under the MIT License.