from request import Request
from bs4 import BeautifulSoup
from beautifulsoup import BeautifulSoupUtil

class Scrape():
    
    def __init__(self: "Scrape", base_url: str) -> None:
        self.base_url = base_url
        
    def get_html(self: "Scrape", resource_path: str, verbose=1, query_param: dict[str, str]=None) -> BeautifulSoup:
        # Fetch Data
        request = Request()
        url = self.base_url + resource_path
        response = request.get(url=url, verbose=verbose)
        # get HTML
        return BeautifulSoupUtil.parse_html(data=response.text, verbose=verbose)