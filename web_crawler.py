from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import argparse
import sys

def find_searched_elements(keyword, page_no):
    """
    This function search the elements in the page by the search keyword.
    With option keyword, it is getting the total number of results for a
    given keyword. And with option keyword and page number, it is to find
    all results for a given keywords on a specified page.
    """
    url_kw = "http://www.shopping.com/products?KW={0}".format(keyword)
    url_pg = "http://www.shopping.com/products~PG-{0}?KW={1}"\
             .format(page_no, keyword)
    page = urlopen(url_kw)
    if page_no is not None:
        page = urlopen(url_pg)
    soup = BeautifulSoup(page.read(), "html.parser")
    lst = soup.findAll('span', attrs={'id': re.compile('^nameQA')})
    if page_no is not None:
        print "List of items: "
        for i in lst:
            print i.text,
    print "Total items: {0}".format(len(lst))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest="page_no", type=int,\
                        help="Page Number")
    parser.add_argument('-k', dest="search_keyword",\
                        type=str, help="Search Keyword")
    args = parser.parse_args()
    if args.search_keyword is None:
        print 'Search keyword need to provide'
        sys.exit()
    find_searched_elements(args.search_keyword, args.page_no)
    
