import requests
from bs4 import BeautifulSoup
import time
import logging

# Prompt the user to choose between square pfps or original pfps
pfp_type = 'square'

# Prompt user for webhook URL
webhook_url = "WEBHOOK-URL-HERE"

# Set up logging
logging.basicConfig(filename='scrape-girl.log', level=logging.ERROR)

# Read list of pages to scrape from file
with open("girl.txt") as f:
    pages = f.readlines()

# Iterate through list of pages
for page in pages:
    # Remove leading and trailing whitespace from page URL
    url = page.strip()

    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all img elements on the page that are NOT inside elements with the "js-blc-t-collection" class
    images = soup.find_all('img', {'class': lambda x: x and 'js-blc-t-collection' not in x.split()})

    # Iterate through the list of images
    for image in images:
        # Get the src attribute of the image
        src = image['src']
        # Replace "superthumb.jpg" with "original.jpg" in the URL if the user chose original pfps
        if pfp_type == 'original':
            src = src.replace('superthumb.jpg', 'original.jpg')
        # Add the URL to the list if it is not already present and does not contain "/avatars/" or "/assets/"
        if '/avatars/' not in src and '/assets/' not in src:
            try:
                # Send image to Discord as embed
                requests.post(webhook_url, json={
                    "embeds": [{
                        "author": {
                            "name": "Girl"
                        },
                        "description": "discord.gg/dress",
                        "footer": {
                            "text": "ara is so hot it's crazy"
                        },
                        "image": {
                            "url": src
                        }
                    }]
                })
            except Exception as e:
                logging.error(f'Error sending image {src}: {e}')

            # Sleep for 5 seconds before sending next image
            time.sleep(10)

    # Print a message to the console indicating that the script is moving to the next page
    print(f'Going to next page: {url}')
