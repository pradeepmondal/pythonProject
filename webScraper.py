# This is a python web scraper
import requests
from bs4 import BeautifulSoup as b

gp = "https://github.com/pradeepmondal"
req = requests.get(gp)
scp = b(req.content, "html.parser")

