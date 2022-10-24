import sys
import requests
import re
from bs4 import BeautifulSoup

def get_links(startLink, depth, numLinks, tabs):
    URL = "https://en.wikipedia.org/"
    page = requests.get(URL + startLink)
    page.raise_for_status()
    
    soup = BeautifulSoup(page.content, "html.parser")
    all_paragraphs = soup.find("p", attrs={"class":None})
    links = all_paragraphs.find_all("a", href=re.compile("(^[/wiki/])"), attrs={"class":None})
    links = [link for link in links if ':' not in link['title']][0:numLinks]
    
    pageTitle = soup.title.text.split("-")[0]
    print("  " * tabs, pageTitle)
    depth -= 1
    tabs += 1

    if depth == 0:
        for link in links:
            print("  " * tabs, link['title'])
    else:
        for link in links:
            get_links(link['href'], depth, numLinks, tabs)    


def main(argv):
    userInput = str(sys.argv[1])
    inputLink = 'wiki/'+ userInput
    depth = int(sys.argv[2])
    numLinks = int(sys.argv[3])
    tabs = 0
    get_links(inputLink, depth, numLinks, tabs)

if __name__ == "__main__":
    main(sys.argv)