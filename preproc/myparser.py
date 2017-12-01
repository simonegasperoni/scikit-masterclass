from bs4 import BeautifulSoup
import urllib.request as ur
#install psycopg, beautifulsoup
#beautifulsoup: html parsing


#returns tags of an html f
def returnsTags(f):
    html = ur.urlopen(f)
    soup = BeautifulSoup(html, "html.parser")
    se = set(tag.name for tag in soup.find_all())
    print(se)


#returns tags content from a tag
def selectsTag(f):
    html = ur.urlopen(f)
    soup = BeautifulSoup(html, "html.parser")
    ps = list(soup.find_all('p'))

    for p in ps:
        print(p)

if __name__ == "__main__":
    selectsTag(
        "file:///C:/Users/s.gasperoni/Desktop/scikit_notes/files/3.html"
    )
