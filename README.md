# PFP Sender Bot

This bot scrapes profile pictures (pfps) from specified pages and sends them to a Discord channel through a webhook. The bot allows you to choose between different types of pfps (e.g., girl, guy, anime) and can send either square pfps or original ones based on your selection. It's built in Python and uses the `requests`, `BeautifulSoup`, and `logging` libraries.

## Features
- Scrapes image URLs from provided pages.
- Customizable PFP types (girl, guy, anime, banner).
- Option to send square or original-sized images.
- Logs any errors that occur during the scraping or image sending process.
- Sends the images to a Discord channel via a webhook as embedded images.

## Requirements

Before using this bot, ensure you have the following dependencies installed:

```bash
pip install requests beautifulsoup4
```

## Setup

1. **Webhook URL:**
   - You will need a Discord webhook URL to send the images. Create a webhook in your Discord server and replace `WEBHOOK-URL-HERE` in the script with your actual webhook URL.

2. **List of Pages:**
   - The script expects a file named `girl.txt` containing a list of URLs (one per line) from which it will scrape the images. You can modify the script to replace `'girl.txt'` with another file name or format.

3. **PFP Type:**
   - The bot prompts you to choose between different PFP types such as `girl`, `guy`, `anime`, or `banner`. This will replace the word `girl` in the `girl.txt` file with your selected type.
   - Additionally, you can specify whether you want square pfps or original pfps.

## Usage

1. Run the bot script:

```bash
python pfp_sender_bot.py
```

2. Choose the type of PFP to scrape (e.g., girl, guy, anime).
3. The script will proceed to scrape the images from the specified URLs and send them to your Discord webhook as embeds.
4. The bot will wait 10 seconds between sending each image to avoid overloading the server.

## Logging

The script logs any errors (e.g., failure to send an image) in a file called `scrape-girl.log`. You can check this file if you encounter issues during scraping or sending.

## Example Log Entry

```
2024-11-30 12:15:23 - ERROR - Error sending image http://example.com/image.jpg: ConnectionError
```

## Customization

- **Modify PFP Types:** You can change the default pfp types by modifying the `replacement_word` logic in the script.
- **Adjust Sleep Time:** You can change the sleep time between requests by modifying the `time.sleep(10)` line.
  
## License

This project is open-source. Feel free to contribute or make changes!
