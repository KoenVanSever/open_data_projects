# Functions used at datahub.io

import urllib3
import bs4
import matplotlib.pyplot as plt

def load_page(domain, search_page):
    http = urllib3.PoolManager(num_pools = 1)
    resp = http.request("GET", f"{domain}{search_page}")
    if resp.status == 200:
        print(f"Search {search_page}: Resource received correctly")
    elif resp.status >= 400 & resp.status < 500:
        print(f"Search {search_page}: Error upon fetching resource, action aborted")
        resp = None
    else:
        print(f"Search {search_page}: Other HTTP respons code (not 200 and not 4xx), action aborted")
        resp = None
    return resp

def process_data_page(resp, search):
    page_string = resp.data.decode("utf8")
    page = bs4.BeautifulSoup(page_string, "html.parser")
    download_tags = page.find_all(class_ = "download")
    link_tags =  []
    for e in download_tags:
        link_tags += e.find_all("a")
    resources = {}
    for tag in link_tags:
        try:
            stripped_inner = tag.string.strip()
            resources[stripped_inner[:stripped_inner.index(" ")]] = tag.get("href")
            print(f"Get available resource path {search}: Data type - file size saved")
        except ValueError:
            print(f"Get available resource path {search}: Data type - file size format error, file ignored")
    return resources

def process_datahub(search, domain = "https://datahub.io"):
    """ Process datahub.io page with default format to [ page response, available data files ]"""
    resp = load_page(domain, search)
    resources = process_data_page(resp, search)
    return resp, resources

def plot_stack_gdp(df):
    plt.clf()
    fig, ax = plt.subplots(1,1)
    ax.stackplot(df.columns, [df.loc[x] for x in df.index])
    labels = df.index
    ax.legend(loc = "center", bbox_to_anchor = (0.5, -0.25), ncol = len(df.columns), labels = labels)
    ax.set_xticks(df.columns)
    ax.xaxis.set_tick_params(rotation = 45)
    return fig, ax

def plot_bar_perc(df):
    plt.clf()
    fig, ax = plt.subplots(1,1)
    for col in df.columns:
        b = 0
        for i, t in enumerate(df[col]):
            ax.bar(x = col, height = t, bottom = b)
            b += t
    labels = df.index
    ax.legend(loc = "center", bbox_to_anchor = (0.5, -0.25), ncol = len(df.columns), labels = labels)
    ax.set_xticks(df.columns)
    ax.xaxis.set_tick_params(rotation = 45)
    return fig, ax