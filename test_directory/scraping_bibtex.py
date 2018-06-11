import bs4
import requests

from test_directory import bibtex

res = requests.get('http://aclanthology.info/events/acl-2016')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

bs4obj = bs4.BeautifulSoup(res.text)

pelem = bs4obj.select('p')[2]
aelem = pelem.select('a')[1]
hrefelem = aelem.get('href')

bibdata = bibtex.getbib(str("http://aclanthology.info/") + str(hrefelem))

#print(pelem)
#print(aelem)
#print(hrefelem)
#print(bibdata)

for i,j in bibdata.items():
    print (i + "=" + j)