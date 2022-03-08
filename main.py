
import requests
import re

from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
from datetime import date


def grab_scripture(soup):
    # Grab the Scripture and the Paragraph

    # This gets the second scripture, which is the active scripture
    get_scripture = soup.find_all("p", class_="themeScrp")[1]
    scripture = get_scripture.text

# This gets the second Paragraph, which is the paragraph that follows the scripture
    get_scripture_paragraph = soup.find_all("p", class_="sb")[1]
    paragraph = get_scripture_paragraph.text.strip()
    return scripture, paragraph


def clean_up_text(paragraph):
    # Regex Command, remove any parentheses in text, and then remove the trailing Watchtower link that begins with w1 or w2 for watchtower year
    modified_paragraph = re.sub(r"\([^()]*\)", "", paragraph)
    modified_paragraph = re.sub(r"\w[1-2](.*)", "", modified_paragraph)
    return modified_paragraph


def combine_text(scripture, modified_paragraph):
    # Combine the text
    final_passage = scripture + "\n" + modified_paragraph
    print(final_passage)
    return final_passage


def text_to_speech(final_text):
    ConvertedTTS = gTTS(final_text)
    ConvertedTTS.save("DailyText.mp3")
    playsound('DailyText.mp3')


if __name__ == "__main__":
    # Grab Date for URL
    today = date.today().strftime('%Y/%m/%d')

# Grab Website with Date
    URL = "https://wol.jw.org/en/wol/h/r1/lp-e/" + today
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser", )

# Run Functions
    scripture, paragraph = grab_scripture(soup)
    clean_text = clean_up_text(paragraph)
    final_text = combine_text(scripture, clean_text)
    text_to_speech(final_text)
