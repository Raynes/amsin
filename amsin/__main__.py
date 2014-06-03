import re

import click
import requests
from bs4 import BeautifulSoup
import pyperclip

@click.command()
@click.argument('url')
def amsin(url):
    """Turn a long amazon link into a short amzn link."""
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    asin = soup.find(text=re.compile('ASIN:')).parent.next_sibling
    url = 'https://amzn.com/' + asin.strip()
    print(url)
    pyperclip.copy(url)
