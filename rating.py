from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.daum.net/') as response:
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    f = open("rating.txt", 'w')
    for anchor in soup.select("a.link_favorsch"):
        data = str(i) + "위 : " + anchor.get_text() + "\n"
        i = i + 1
        f.write(data)
    f.close()