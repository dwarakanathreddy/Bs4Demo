from bs4 import BeautifulSoup as bs
import requests


def get_canonical_url(url):
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    for a in soup.find_all('link', href=True,rel='canonical'):
        print("For the URL: " + str(url) + " Found the canonical URL value:", a['href'])


url1 = "https://www.shopify.com/partners/blog/canonical-urls"
get_canonical_url(url1)
url2 = "https://moz.com/learn/seo/canonicalization"
get_canonical_url(url2)
url3 = "https://www.bigcommerce.com/ecommerce-answers/what-is-a-canonical-url-what-online-retailers-need-to-know-about-the-canonical-tag/"
get_canonical_url(url3)
