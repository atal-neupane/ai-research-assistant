import arxiv
from urllib.request import urlretrieve
import os
import csv

# Extract arxiv_ids from the mainfest.csv file
with open("manifest.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    arxiv_ids = [row["arxiv_id"] for row in reader if row["arxiv_id"]]

PATH = "data/latex/"

os.makedirs(PATH, exist_ok=True)

# Construct the default API client
client = arxiv.Client()

# Search for the given ids
search = arxiv.Search(id_list=arxiv_ids)

# papers is a generator
papers = client.results(search)
for paper in papers:
    destination = os.path.join(PATH, f"{paper.get_short_id()}.tar.gz")
    if not os.path.exists(destination):
        #Download the LaTeX source only if it does not exist
        urlretrieve(paper.source_url(), destination)
        print(f"Downloaded {destination}")
    else:
        print(f"{destination} already exists")  