"""
Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных (https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv количество животных на каждую букву алфавита. 
Содержимое результирующего файла:

А,642
Б,412
В,....

Примечание:
анализ текста производить не нужно, считается любая запись из категории 
(в ней может быть не только название, но и, например, род)

wikiperdia.org/w/index.php?title=Категория:Животные_по_алфавиту&from=<b>А<%2Fb>
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
from collections import defaultdict

# URL of the main category page
# url = "https://en.wikipedia.org/wiki/List_of_animal_names"
url = "https://en.wikipedia.org/wiki/List_of_animal_names"

# Send HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200 = OK)
if response.status_code == 200:
    
    html = response.text
    print("Page downloaded successfully.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Get the main content div
content_div = soup.find("div", id="mw-content-text")

# Find all links within the main content
animal_links = []
for tag in content_div.find_all("a", href=True):
    href = tag['href']
    if href.startswith("/wiki/") and ":" not in href:
        animal_links.append(href)

# Dictionary to count link occurrences by starting letter
letter_counts = defaultdict(int)

for link in animal_links:
    # Remove the /wiki/ part
    title = link.replace("/wiki/", "")
    
    # Skip empty or malformed titles
    if not title or not title[0].isalpha():
        continue

    # Count based on first uppercase letter
    first_letter = title[0].upper()
    letter_counts[first_letter] += 1

# Sort the result by letter
for letter in sorted(letter_counts):
    print(f"{letter}: {letter_counts[letter]}")