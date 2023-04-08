import requests
from bs4 import BeautifulSoup
import telegram
import schedule
# Initialize the Telegram bot
bot = telegram.Bot(token='')

# Define the URL to monitor
url = 'https://example.com'

# Initialize the previous content to compare with
prev_content = ''

def check_website():
    global prev_content
    response = requests.get(url)
    content = response.text
    if content != prev_content:
        # Send a notification to the user
        bot.send_message(chat_id='your_chat_id', text='The website has been updated!')
        prev_content = content

# Schedule the check_website function to run every hour
schedule.every().hour.do(check_website)

while True:
    schedule.run_pending()