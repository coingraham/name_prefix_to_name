import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint

PREFIX = "https://docs.aws.amazon.com/service-authorization/latest/reference"
URL = "{}/reference_policies_actions-resources-contextkeys.html".format(PREFIX)
namespace_service = {}

html_page = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(html_page, features="html.parser")
highlights = soup.body.find('div', attrs={'class': 'highlights'})
links = highlights.findAll('a')

for link in links:
    service_name = link.get_text()
    uri = link["href"].split("/")[1]

    follow_page = urllib.request.urlopen("{}/{}".format(PREFIX, uri)).read()
    new_soup = BeautifulSoup(follow_page, features="html.parser")
    service_prefix = new_soup.body.find('code', attrs={'class': 'code'}).get_text()
    namespace_service[service_prefix] = service_name

pprint(namespace_service)
