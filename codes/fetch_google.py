from scholarly import scholarly
import pandas as pd

keyword = "Federal Statistical Research Data Centers" # Search keyword

def fetch_google_scholar(query, num_results=500):
    """ From Google Scholar fetch num_results=500 papers """
    papers = []
    search_results = scholarly.search_pubs(query)

    for i in range(num_results):
        try:
            paper = next(search_results)  # Enumerate the papers
            papers.append({
                "Title": paper.get("bib", {}).get("title", "N/A"),
                "Authors": paper.get("bib", {}).get("author", "N/A"),
                "Year": paper.get("bib", {}).get("pub_year", "N/A"),
                "Venue": paper.get("bib", {}).get("venue", "N/A"),
                "DOI": paper.get("pub_url", "N/A")
            })
        except StopIteration:
            break

    return papers

def save_to_csv(data, filename="data/google_data.csv"):
    """ Store the data into a CSV file """
    df = pd.DataFrame(data) # Transform into DataFrame
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Success! Data is stored into {filename}")

if __name__ == "__main__":
    papers = fetch_google_scholar(keyword, num_results=500)

    if papers: # Results are valid
        save_to_csv(papers)
        print("Fetch successfully!")
        print(pd.DataFrame(papers))
    else:
        print("No papers found!")
