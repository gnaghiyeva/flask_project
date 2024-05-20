import requests
from bs4 import BeautifulSoup


def crawl(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')

            if href and href.startswith('https://smartjob.az/'):
                yield 'https://smartjob.az/' + href

    except requests.RequestException as e:
        print(f"Error crawling {url}: {e}")


# Test için kullanılacak URL
url = 'https://smartjob.az/vacancies'
for link in crawl(url):
    print(link)
    # İstediğiniz işlemi burada yapabilirsiniz
