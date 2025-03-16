import requests
import pandas as pd

# Crossref website
CROSSREF_URL = "https://api.crossref.org/works"
keyword = "Federal Statistical Research Data Centers" # Search keyword

def fetch_crossref_data(query, num_results=500):
    """ From Crossref API fetch num_results=500 papers """
    params = {
        "query": query,
        "rows": num_results,
        "select": "title,author,issued,DOI,container-title",
    }
    
    response = requests.get(CROSSREF_URL, params=params) # Visit Crossref website and search

    if response.status_code == 200: # Check if the website responses successfully
        data = response.json() # Transform json data into dictionary
        papers = [] # Initialize the results

        for item in data.get("message", {}).get("items", []):
            # Enumerate information of papers
            title = item.get("title", ["N/A"])[0]
            authors = ", ".join([author.get("family", "Unknown") for author in item.get("author", [])])
            year = item.get("issued", {}).get("date-parts", [[None]])[0][0]
            venue = item.get("container-title", ["N/A"])[0]
            doi = item.get("DOI", "N/A")
            
            # Store the papers, one paper with one dictionary part
            papers.append({
                "Title": title,
                "Authors": authors,
                "Year": year,
                "Venue": venue,
                "DOI": f"https://doi.org/{doi}" if doi != "N/A" else "N/A"
            })
        
        return papers
    else:
        print(f"Request fails with status code: {response.status_code}")
        return []

def save_to_csv(data, filename="data/crossref_data.csv"):
    """ Store the data into a CSV file """
    df = pd.DataFrame(data) # Transform into DataFrame
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Success! Data is stored into {filename}")

if __name__ == "__main__":
    papers = fetch_crossref_data(keyword, num_results=500) # Call on the searching function

    if papers: # Results are valid
        save_to_csv(papers)
        print("Fetch successfully!")
        print(pd.DataFrame(papers))
    else:
        print("No papers found!")