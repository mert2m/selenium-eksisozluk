import random
import time
from selenium import webdriver

browser = webdriver.Firefox()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
    randomPage = random.randint(1, 1290)
    newurl = url + str(randomPage)
    browser.get(newurl)
    elements = browser.find_elements_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(5)
    pageCount += 1

with open("entries.txt", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(pageCount) + ".\n" + entry + "\n")
        file.write("*******************")
        pageCount += 1

for entry in entries:
    print(str(entryCount) + "*****************************")
    print(entry)

browser.close()
