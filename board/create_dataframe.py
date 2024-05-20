import requests
from bs4 import BeautifulSoup
import pandas as pd


def create_dataframe(url):
    job_titles = []
    company_names = []
    salary_ranges = []
    job_descriptions = []
    img_urls = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Tüm iş ilanlarını bul
        job_items = soup.find_all('div', class_='item-click')

        for job_item in job_items:
            # İş başlığı
            job_title = job_item.find('div', class_='brows-job-position').h3.a.text.strip()
            job_titles.append(job_title)

            # Şirket adı
            company_name = job_item.find('span', class_='company-title').a.text.strip()
            company_names.append(company_name)

            # Maaş aralığı
            salary_range = job_item.find('div', class_='hide-on-pc salary-mob').text.strip()
            salary_ranges.append(salary_range)

            # İş açıklaması
            job_description = job_item.find('div', class_='sub-info').text.strip()
            job_descriptions.append(job_description)

            # Resim URL'si
            img_tag = job_item.find('div', class_='brows-job-company-img').find('img')
            if img_tag:
                img_src = img_tag['src']
                img_urls.append(img_src)
            else:
                img_urls.append(None)

    except requests.RequestException as e:
        print("Hata:", e)

    # Verileri Pandas DataFrame'ine dönüştürme
    df = pd.DataFrame({
        'job_title': job_titles,
        'company_name': company_names,
        'salary_range': salary_ranges,
        'job_description': job_descriptions,
        'img_tag': img_urls
    })

    return df


# Test için kullanılacak URL
url = "https://smartjob.az/vacancies"
dataframe = create_dataframe(url)
print(dataframe)


