import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://arxiv.org/search/?query=machine+learning&searchtype=all&source=header"

papers = []

for page in range(0, 25):
    print(f"Scraping page {page+1}...")
    url = f"{base_url}&start={page*50}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("li", class_="arxiv-result")

    for result in results:

        title_tag = result.find("p", class_="title is-5 mathjax")
        title = title_tag.text.strip().replace("\n", " ").replace(",", ";") if title_tag else "N/A"

        authors_tag = result.find("p", class_="authors")
        authors = authors_tag.text.replace("Authors:", "").strip().replace("\n", " ").replace(",", ";") if authors_tag else "N/A"

        category_tag = result.find("span", class_="tag is-small is-link tooltip is-tooltip-top")
        category = category_tag.text.strip() if category_tag else "N/A"

        link_tag = result.find("p", class_="list-title is-inline-block")
        link = link_tag.find("a")["href"].strip() if link_tag and link_tag.find("a") else "N/A"

        papers.append({
            "Title": " ".join(title.split()),
            "Authors": " ".join(authors.split()),
            "Category": " ".join(category.split()),
            "Link": link
        })

    time.sleep(2)

df = pd.DataFrame(papers)
df.to_csv("arxiv_papers.csv", index=False, encoding="utf-8-sig")
