import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url):
    try:
        # Fetch the webpage content
        response = requests.get(url, verify=True)
        # response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text content
        text_content = soup.get_text(separator='\n', strip=True)  # Separate text by newlines
        return text_content
    except Exception as e:
        return f"Error scraping the URL: {e}"

# Example usage
url = "https://timesofindia.indiatimes.com/world/us/photos-how-wildfires-ravaged-through-southern-california/photostory/117072435.cms"  # Replace with the URL you want to scrape
text_content = scrape_text_from_url(url)
print(text_content)