import time
from selenium import webdriver

def get_entries(url, start_page, end_page):
    browser = webdriver.Firefox()  # You can change to different browsers here.
    entries = []

    try:
        for page_num in range(start_page, end_page + 1):
            current_page = f"{url}{page_num}"
            browser.get(current_page)
            elements = browser.find_elements_by_css_selector(".content")
            for element in elements:
                entries.append(element.text)
            time.sleep(5)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        browser.quit()

    return entries

def save_entries_to_file(entries):
    with open("entries.txt", "w", encoding="UTF-8") as file:
        for idx, entry in enumerate(entries, start=1):
            file.write(f"{idx}.\n{entry}\n")
            file.write("*******************\n")

def print_entries(entries):
    for idx, entry in enumerate(entries, start=1):
        print(f"{idx}*****************************")
        print(entry)

def main():
    url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
    try:
        start_page = int(input("Starting page number: "))
        end_page = int(input("Ending page number: "))
        if start_page <= 0 or end_page <= 0 or start_page > end_page:
            raise ValueError("Invalid page range.")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        entries = get_entries(url, start_page, end_page)
        save_entries_to_file(entries)
        print_entries(entries)

if __name__ == "__main__":
    main()
