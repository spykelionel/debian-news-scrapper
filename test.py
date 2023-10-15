import unittest
from unittest.mock import patch
from main import DebianNewsScraper

class TestDebianNewsScraper(unittest.TestCase):
    def test_save(self):
        # Mock the requests library to simulate a successful response
        with patch('main.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = """
                <html>
                    <div id="content">
                        <p>News item 1</p>
                        <p>News item 2</p>
                    </div>
                </html>
            """
            
            url = "https://wiki.debian.org/News"
            scraper = DebianNewsScraper(url)
            
            file_name = "test.log"
            scraper.save(file_name)
            
            # Verify that the file is created and contains the expected content
            with open(file_name, "r", encoding="utf-8") as f:
                news_content = f.read()
                expected_content = "News item 1\n\nNews item 2"
                self.assertEqual(news_content, expected_content)
            
    def test_scrape_failed_request(self):
        # Mock the requests library to simulate a failed request
        with patch('main.requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            
            url = "https://wiki.debian.org/News"
            scraper = DebianNewsScraper(url)
            
            # Verify that an exception is raised when the request fails
            with self.assertRaises(Exception):
                scraper.scrape()
            
if __name__ == "__main__":
    unittest.main()