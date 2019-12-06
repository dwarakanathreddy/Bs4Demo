from bs4 import BeautifulSoup as bs #library for reading and parsing the html content
import requests # requests module to get website

# start of the method here
def get_canonical_url(url):
    page = requests.get(url)
    # the html along with some other stuff is loaded in to the page variable
    soup = bs(page.content, 'html.parser') # here we extract only html content, removing unnecessary things downloaded from the requests
    for a in soup.find_all('link', href=True,rel='canonical'):
        #here we loop for all the link tags and check for canonical rel values
        #if the condition is met, then we print, there might be many href, not all are canonical values
        print("For the URL: " + str(url) + " Found the canonical URL value:", a['href'])


url1 = "https://www.shopify.com/partners/blog/canonical-urls"
get_canonical_url(url1)
url2 = "https://moz.com/learn/seo/canonicalization"
get_canonical_url(url2)
url3 = "https://www.bigcommerce.com/ecommerce-answers/what-is-a-canonical-url-what-online-retailers-need-to-know-about-the-canonical-tag/"
get_canonical_url(url3)
