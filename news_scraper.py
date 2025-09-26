import requests
from bs4 import BeautifulSoup

# URL of the news site (BBC in this case)
URL = "https://www.bbc.com/news"

# Send a GET request to the website
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all headline tags (adjusted for BBC's structure)
    # Typically, headlines are in <h3> tags with specific classes
    headline_tags = soup.find_all(['h3', 'h2'])

    # Extract and clean the text
    headlines = []
    for tag in headline_tags:
        text = tag.get_text(strip=True)
        if text and len(text) > 10:  # Filter short/empty headlines
            headlines.append(text)

    # Remove duplicates
    unique_headlines = list(dict.fromkeys(headlines))

    # Save headlines to a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for idx, headline in enumerate(unique_headlines, start=1):
            file.write(f"{idx}. {headline}\n")

    print(f"✅ {len(unique_headlines)} headlines saved to 'headlines.txt'")

else:
    print("❌ Failed to retrieve the page. Status Code:", response.status_code)
