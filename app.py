import requests
from bs4 import BeautifulSoup

# URL of the Debian Wiki News page
url = "https://wiki.debian.org/News"

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the content section of the page
    content_section = soup.find(id="content")

    # Find all the paragraphs within the content section
    paragraphs = content_section.find_all("p")

    # Create a Markdown file to write the content
    with open("debian_news.md", "w", encoding="utf-8") as file:
        for paragraph in paragraphs:
            # Write each paragraph to the Markdown file
            file.write(paragraph.get_text())
            file.write("\n\n")

    print("Debian News successfully written to debian_news.md.")
else:
    print("Failed to retrieve Debian News. Please check the URL or your internet connection.")