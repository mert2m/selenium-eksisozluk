import elements as elements
from selenium import webdriver
import random
import time

browser = webdriver.Firefox()
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pageCount = 1
entries = []
entryCount = 1
while pageCount<=10:
    randomPage = random.randint(1,1290)
    newurl = url + str(randomPage)
    browser.get(newurl)
    element = browser.find_element_by_css_selector(".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(5)
    pageCount +=1
with open("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(pageCount)+".\n"+ entry + "\n")
        file.write("*******************")
        pageCount += 1
for entry in entries:
    print(str(entryCount)+ "*****************************")
    print(element.txt)
browser.close()
#browser.get(url)
#time.sleep(10)
# elements = browser.find_elements_by_css_selector(".content")
# for element in elements:
#     print("************************")
#     print(element.text)
browser.close()