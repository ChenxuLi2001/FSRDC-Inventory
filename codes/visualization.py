import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV data files
df = pd.read_csv("data/merged_data.csv")

# Set the graph style
sns.set_theme(style="whitegrid")

# Figure of quantity change
plt.figure(figsize=(10, 5))
paper_counts = df["Year"].value_counts().sort_index() # Use "Year" as the statistical index
sns.lineplot(x=paper_counts.index, y=paper_counts.values, marker="o")
plt.xlabel("Year")
plt.ylabel("Paper Number")
plt.title("Trend of FSRDC Research Paper Quantity Change")
plt.xticks(rotation=45)
plt.grid()
plt.savefig("data/Quantity_change.png")  # Store the figure
plt.show()

# Figure of popular container statistics
plt.figure(figsize=(12, 6))
venue_counts = df["Venue"].value_counts().nlargest(10)  # Find 10 containers with the most FSRDC papers
sns.barplot(x=venue_counts.values, y=venue_counts.index, palette="Blues_r")
plt.xlabel("Paper Number")
plt.ylabel("Titile of Container")
plt.title("Most Popular Containers Publishing FSRDC Papers")
plt.savefig("data/Containers.png")
plt.show()

# Figure of DOI proportion statistics based on Google Scholar
has_doi = df["DOI"].apply(lambda x: isinstance(x, str) and "N/A" not in x and bool(x)).value_counts()
plt.figure(figsize=(6, 6))
plt.pie(has_doi, labels=["Has DOI", "No DOI"], autopct="%1.1f%%", colors=["#4CAF50", "#FF5733"])
plt.title("DOI proportion statistics")
plt.savefig("data/doi_proportion.png")
plt.show()