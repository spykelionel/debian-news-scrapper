import requests
from bs4 import BeautifulSoup

class DebianNewsScraper:
    def __init__(self, url):
        self.url = url
    
    def scrape(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.HTTPError as e:
            raise Exception("Failed to retrieve Debian News. Error: {}".format(e))
        except requests.ConnectionError as e:
            raise Exception("Failed to connect to the Debian News website. Error: {}".format(e))
        
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find(id="content")
        paragraphs = content.find_all("p")
        news_paragraphs = [p.get_text() for p in paragraphs]
        
        return "\n\n".join(news_paragraphs)
            
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