import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape_web_article(self):
        response = requests.get(self.url)

        # this constructor is used to define the kind of scrape we want, in this case -> 'html.parser'
        parser_to_use = 'html.parser'
        html_soup = BeautifulSoup(response.text, parser_to_use)

        # get all <p> html tag
        return html_soup.find_all('p')

    def extract_text_from_paragraph(self, html_paragraphs):
        result = ""
        for paragraph in html_paragraphs:
            result += paragraph.get_text() + "\n"

        return result

