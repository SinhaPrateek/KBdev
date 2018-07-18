import requests
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
def getbib(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))

    bibtext = res.text

    def customizations(record):
        """Use some functions delivered by the library

        :param record: a record
        :returns: -- customized record
        """
        record = type(record)
        record = author(record)
        record = editor(record)
        record = journal(record)
        record = keyword(record)
        record = link(record)
        record = page_double_hyphen(record)
        record = doi(record)
        return record

    print(bibtext)
    parser = BibTexParser()
    parser.customization = customizations
    bib_database = bibtexparser.loads(bibtext,parser = parser)
    #print(bib_database)
    return bib_database.entries[0]
    """
    for i, j in bib_database.entries[0].items():
        print(i + "=" + j)
    """



