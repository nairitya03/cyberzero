from bs4 import BeautifulSoup

class SoupParser:
    def __init__(self, html, parser):
        self.soup = BeautifulSoup(html, parser).find('body')

    def parse (self):
        self.soup = self.cleaner(self)
        return self.soup
    
    @staticmethod
    def cleaner(self):
        #Remove the header and footer elements from the HTML document.
        for elem in self.soup.find_all(['header', 'footer', 'script', 'img', 'a', 'tags']) + \
            self.soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') == '#Archive') + \
            self.soup.find_all('a', href=True): 
            if elem: elem.decompose()

        for elem in self.soup.find_all(string=lambda t: t.startswith('Labels ------') or t.startswith('*') or (t and ('\ue5c5' in t or '\ue2c7' in t))):
            elem.extract()
            
        for img in self.soup.find_all('img'):
            if img.get('src') and img.get('src').startswith('data:image'):
                img.decompose()

        return self.soup