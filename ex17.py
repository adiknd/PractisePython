import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
list_of_headings = set()
soup = BeautifulSoup(r_html, "html.parser")
for heading in soup.find_all(class_="story-heading"):
        list_of_headings.add(heading.text.strip())

for i in list_of_headings:
    print(i)

