import requests
from python.helpers.soup_parser import SoupParser
from python.helpers.markdown import Markdown


class WebScrape:
    def __init__(self):
        self.response =""
        pass

    def scrape(self, queries):
        
        for query in queries:
            title, url = query["title"], query["href"]
            try:
                http_response = requests.get(url)
                http_response.raise_for_status()
                body = SoupParser(http_response.text, "html.parser").parse()
                self.response +=  Markdown(title, url, body).clean()
            except requests.exceptions.RequestException:
                pass  # or log the error if needed
        return self.response