import requests
from bs4 import BeautifulSoup


def scrape_page(url):
    jobs = []  # Initialize an empty list to store job data

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tüm iş ilanlarını bul
        job_items = soup.find_all('div', class_='item-click')

        for job_item in job_items:
            job = {}  # Create a dictionary to store job details

            # İş başlığı
            job['job_title'] = job_item.find('div', class_='brows-job-position').h3.a.text.strip()

            # Şirket adı
            job['company_name'] = job_item.find('span', class_='company-title').a.text.strip()

            # Maaş aralığı
            job['salary_range'] = job_item.find('div', class_='hide-on-pc salary-mob').text.strip()

            # İş açıklaması
            job['job_description'] = job_item.find('div', class_='sub-info').text.strip()

            # Add the job to the list of jobs
            jobs.append(job)

    except requests.RequestException as e:
        print("Hata:", e)

    return jobs



