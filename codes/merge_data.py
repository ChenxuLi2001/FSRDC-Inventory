import pandas as pd

# Read the existing data files
crossref_df = pd.read_csv("data/crossref_data.csv")
google_df = pd.read_csv("data/google_data.csv")

# Distinguish the data sources
crossref_df["Source"] = "Crossref"
google_df["Source"] = "Google Scholar"

# Fill NaN values in Google Scholar DOI, avoiding errors
google_df["DOI"] = google_df["DOI"].fillna("N/A")

# Eliminate duplicates by DOI
google_df = google_df[~google_df["DOI"].isin(crossref_df["DOI"])]

# Eliminate duplicates by Title
google_df = google_df[~google_df["Title"].isin(crossref_df["Title"])]

# Eliminate duplicates by Author & Year
google_df = google_df[~(
    (google_df["Authors"].isin(crossref_df["Authors"])) & 
    (google_df["Year"].isin(crossref_df["Year"]))
)]

# Merge the data files
merged_df = pd.concat([crossref_df, google_df], ignore_index=True)

# Store the merged data file
merged_df.to_csv("data/merged_data.csv", index=False, encoding="utf-8")