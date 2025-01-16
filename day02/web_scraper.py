import requests
from bs4 import BeautifulSoup

url = "http://www.scrapethissite.com/pages/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

data = soup.find_all("h2")

with open("data.txt", "w") as file:
    file.write(str(data))

