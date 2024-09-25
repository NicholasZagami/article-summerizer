import scraper

url = 'https://vidhi-chugh.medium.com/how-to-scrape-the-web-effectively-d9113420dabe'

s = scraper.WebScraper(url)

result = s.scrape_web_article()
text_result = s.extract_text_from_paragraph(result)
print(text_result)