# netflixGraph.py
# Author: Santiago Lizarraga
# May 13, 2025
#
# This script reads a JSON file containing Netflix Top 10 show data,
# extracts the number of views for each show, and generates a bar graph
# visualizing view counts. The graph is saved as an image and can be
# used to compare relative popularity based on Netflix's reported view metrics.

import json
import matplotlib.pyplot as plt

# Load the Netflix JSON data
file_path = "data_Netflix.json"  
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

titles = [entry["title"].split(":")[0] for entry in data]
views = [int(entry["views"].replace(",", "")) / 1_000_000 for entry in data]


plt.figure(figsize=(10, 6))
plt.barh(titles, views, color='mediumseagreen')
plt.xlabel("Views (in millions)")
plt.title("Netflix Top 10 Shows by View Count")
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.savefig("netflix_views_graph.png")
plt.show()
