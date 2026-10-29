import arxiv
from urllib.request import urlretrieve
import os
import csv

# Extract arxiv_ids from the mainfest.csv file
with open("manifest.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    arxiv_ids = [row["arxiv_id"] for row in reader]

PATH = "data/pdfs/"

# Construct the default API client
client = arxiv.Client()

# Search for the given ids
search = arxiv.Search(id_list=arxiv_ids)

# papers is a generator
papers = client.results(search)
for paper in papers:
    destination = f"{PATH}{paper.title}.pdf"
    if not os.path.exists(destination):
        # Download the PDF only if it does not exits
        urlretrieve(paper.pdf_url, f"{destination}")
        print(f"Downloaded {destination}")
    else:
        print(f"{destination} already exits")
