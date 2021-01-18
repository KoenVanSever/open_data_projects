#! /home/koenvs/Documents/coding/roosje_graphs/plotenv/bin/python

from requests_html import AsyncHTMLSession, HTMLSession
import requests
from pathlib import Path
import bs4

session = HTMLSession()
r = session.get("https://ec.europa.eu/eurostat/web/main/data/database")
r.html.render(retries=4, wait=0.1)
print(len(r.html.links))
page = bs4.BeautifulSoup(r.text)
print(page.find_all("a"))
# print(any(map(lambda x: x.__contains__("Bulk"), r.html.absolute_links)))
print(list(filter(lambda x: x.__contains__("javascript"), r.html.links)))
# with open(Path(".", "eurostat", "page_text.html"), "w") as f:
#    f.write(r.text)
