import requests
from threading import Thread
from bs4 import BeautifulSoup


urls = [
    "https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/langchain/quickstart",
    "https://docs.langchain.com/oss/python/langchain/models",
]


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Length of the content from {url} is : {len(soup.text)}")


threads = []

for url in urls:
    thread = Thread(target=scrape_website, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have completed their tasks.")
