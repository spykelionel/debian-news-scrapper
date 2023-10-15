import requests
from bs4 import BeautifulSoup

class DebianNewsScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            content = soup.find(id="content")
            paragraphs = content.find_all("p")
            
            news_items = [p.get_text() for p in paragraphs]
            return "\n\n".join(news_items)
        else:
            raise Exception("Failed to retrieve Debian News")
            
    def save(self, file_name):
        news = self.scrape()
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(news)
        
if __name__ == "__main__":
    url = "https://wiki.debian.org/News"
    scraper = DebianNewsScraper(url)
    file_name = "README.md"
    scraper.save(file_name)
    print("Debian News saved to", file_name)