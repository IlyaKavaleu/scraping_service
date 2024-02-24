import json
from random import randint
import requests
import codecs
from bs4 import BeautifulSoup as BS
from utils import from_cyrillic_to_eng

__all__ = ('work', 'dou', 'jooble', 'ria',
           'work_java', 'dou_java', 'jooble_java', 'ria_java',
           'work_c_plus_plus', 'dou_c_plus_plus', 'jooble_c_plus_plus', 'ria_c_plus_plus',
           'jooble_python_gdansk', 'jooble_java_gdansk', 'jooble_c_plus_plus_gdansk',
           'dou_python_gdansk', 'dou_java_gdansk', 'dou_c_plus_plus_gdansk'
           )

headers = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    },
    {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                      "like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"
    },
]


def work(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://www.work.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_list:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    logo = div.find('')
                    if logo:
                        company = logo['alt']
                    jobs.append({
                        'title': title.text,
                        'url': domain + href,
                        'description': content,
                        'company': company,
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'div does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def work_java(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://www.work.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_list:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    logo = div.find('')
                    if logo:
                        company = logo['alt']
                    jobs.append({
                        'title': title.text,
                        'url': domain + href,
                        'description': content,
                        'company': company,
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'div does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def work_c_plus_plus(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://www.work.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id='pjax-job-list')
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'job-link'})
                for div in div_list:
                    title = div.find('h2')
                    href = title.a['href']
                    content = div.p.text
                    company = 'No name'
                    logo = div.find('')
                    if logo:
                        company = logo['alt']
                    jobs.append({
                        'title': title.text,
                        'url': domain + href,
                        'description': content,
                        'company': company,
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'div does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def jooble(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://ua.jooble.org/"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'infinite-scroll-component ZbPfXY _serpContentBlock'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ojoFrF rHG1ci V5WdkE'})
                for date in dates:
                    title = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})
                    href = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})['href']
                    content = date.find('div', attrs={'class': 'PAM72f'})
                    company = date.find('p', attrs={'class': 'z6WlhX'})
                    logo = date.find('img', attrs={'class': '_3hk3rl'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text if company else '',
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def jooble_java(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://ua.jooble.org/"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'infinite-scroll-component ZbPfXY _serpContentBlock'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ojoFrF rHG1ci V5WdkE'})
                for date in dates:
                    title = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})
                    print(title)
                    href = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})['href']
                    content = date.find('div', attrs={'class': 'PAM72f'})
                    company = date.find('p', attrs={'class': 'z6WlhX'})

                    logo = date.find('img', attrs={'class': '_3hk3rl'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def jooble_c_plus_plus(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://ua.jooble.org/"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'infinite-scroll-component ZbPfXY _serpContentBlock'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ojoFrF rHG1ci V5WdkE'})
                for date in dates:
                    title = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})
                    print(title)
                    href = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})['href']
                    content = date.find('div', attrs={'class': 'PAM72f'})
                    company = date.find('p', attrs={'class': 'z6WlhX'})

                    logo = date.find('img', attrs={'class': '_3hk3rl'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def dou(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://jobs.dou.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': 'vacancyListId'})
            if main_div:
                dates = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for date in dates:
                    title = date.find('div', class_='title').find('a', attrs={'class': 'vt'})
                    href = date.find('div', class_='title').a['href']
                    content = date.find('div', attrs={'class': 'sh-info'})
                    company = date.find('div', attrs={'class': 'title'}).find('a', attrs={'class': 'company'})
                    logo = date.find('div', attrs={'class': 'title'}).find('img', attrs={'class': 'f-i'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })

            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def dou_java(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://jobs.dou.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': 'vacancyListId'})
            if main_div:
                dates = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for date in dates:
                    title = date.find('div', class_='title').find('a', attrs={'class': 'vt'})
                    href = date.find('div', class_='title').a['href']
                    content = date.find('div', attrs={'class': 'sh-info'})
                    company = date.find('div', attrs={'class': 'title'}).find('a', attrs={'class': 'company'})
                    logo = date.find('div', attrs={'class': 'title'}).find('img', attrs={'class': 'f-i'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })

            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def dou_c_plus_plus(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://jobs.dou.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': 'vacancyListId'})
            if main_div:
                dates = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for date in dates:
                    title = date.find('div', class_='title').find('a', attrs={'class': 'vt'})
                    href = date.find('div', class_='title').a['href']
                    content = date.find('div', attrs={'class': 'sh-info'})
                    company = date.find('div', attrs={'class': 'title'}).find('a', attrs={'class': 'company'})
                    logo = date.find('div', attrs={'class': 'title'}).find('img', attrs={'class': 'f-i'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })

            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def ria(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://robota.ua/ru/zapros/python/kyiv"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'clearfix search-items'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ticket-clean user-12917558'})
                for date in dates:
                    title = date.find('span', attrs={'class': 'ticket-subtitle'})
                    href = date.find('a', attrs={'class': 'ticket-title'})['href']
                    content = 'No data'
                    company = 'EPAM'
                    logo = date.find('img', attrs={'class': 'img-ticket'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content,
                        'company': company,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def ria_java(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://robota.ua/ru/zapros/python/kyiv"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'clearfix search-items'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ticket-clean user-12917558'})
                for date in dates:
                    title = date.find('span', attrs={'class': 'ticket-subtitle'})
                    href = date.find('a', attrs={'class': 'ticket-title'})['href']
                    content = 'No data'
                    company = 'EPAM'
                    logo = date.find('img', attrs={'class': 'img-ticket'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content,
                        'company': company,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def ria_c_plus_plus(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://robota.ua/ru/zapros/python/kyiv"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'clearfix search-items'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ticket-clean user-12917558'})
                for date in dates:
                    title = date.find('span', attrs={'class': 'ticket-subtitle'})
                    href = date.find('a', attrs={'class': 'ticket-title'})['href']
                    content = 'No data'
                    company = 'EPAM'
                    logo = date.find('img', attrs={'class': 'img-ticket'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content,
                        'company': company,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors













def jooble_python_gdansk(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://ua.jooble.org/"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'infinite-scroll-component ZbPfXY _serpContentBlock'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ojoFrF rHG1ci V5WdkE'})
                for date in dates:
                    title = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})
                    href = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})['href']
                    content = date.find('div', attrs={'class': 'PAM72f'})
                    company = date.find('p', attrs={'class': 'z6WlhX'})
                    logo = date.find('img', attrs={'class': '_3hk3rl'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text if company else '',
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def jooble_java_gdansk(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://ua.jooble.org/"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'infinite-scroll-component ZbPfXY _serpContentBlock'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ojoFrF rHG1ci V5WdkE'})
                for date in dates:
                    title = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})
                    print(title)
                    href = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})['href']
                    content = date.find('div', attrs={'class': 'PAM72f'})
                    company = date.find('p', attrs={'class': 'z6WlhX'})

                    logo = date.find('img', attrs={'class': '_3hk3rl'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def jooble_c_plus_plus_gdansk(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://ua.jooble.org/"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'infinite-scroll-component ZbPfXY _serpContentBlock'})
            if main_div:
                dates = main_div.find_all('div', attrs={'class': 'ojoFrF rHG1ci V5WdkE'})
                for date in dates:
                    title = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})
                    print(title)
                    href = date.find('a', attrs={'class': '_8w9Ce2 tUC4Fj hyperlink_appearance_undefined _6i4Nb0 g2JQMz'})['href']
                    content = date.find('div', attrs={'class': 'PAM72f'})
                    company = date.find('p', attrs={'class': 'z6WlhX'})

                    logo = date.find('img', attrs={'class': '_3hk3rl'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })
            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def dou_python_gdansk(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://jobs.dou.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': 'vacancyListId'})
            if main_div:
                dates = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for date in dates:
                    title = date.find('div', class_='title').find('a', attrs={'class': 'vt'})
                    href = date.find('div', class_='title').a['href']
                    content = date.find('div', attrs={'class': 'sh-info'})
                    company = date.find('div', attrs={'class': 'title'}).find('a', attrs={'class': 'company'})
                    logo = date.find('div', attrs={'class': 'title'}).find('img', attrs={'class': 'f-i'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })

            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def dou_java_gdansk(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://jobs.dou.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': 'vacancyListId'})
            if main_div:
                dates = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for date in dates:
                    title = date.find('div', class_='title').find('a', attrs={'class': 'vt'})
                    href = date.find('div', class_='title').a['href']
                    content = date.find('div', attrs={'class': 'sh-info'})
                    company = date.find('div', attrs={'class': 'title'}).find('a', attrs={'class': 'company'})
                    logo = date.find('div', attrs={'class': 'title'}).find('img', attrs={'class': 'f-i'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })

            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors


def dou_c_plus_plus_gdansk(url, city=None, language=None):
    jobs = []
    errors = []
    domain = "https://jobs.dou.ua"
    if url:
        resp = requests.get(url, headers=headers[randint(0, 1)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'id': 'vacancyListId'})
            if main_div:
                dates = main_div.find_all('li', attrs={'class': 'l-vacancy'})
                for date in dates:
                    title = date.find('div', class_='title').find('a', attrs={'class': 'vt'})
                    href = date.find('div', class_='title').a['href']
                    content = date.find('div', attrs={'class': 'sh-info'})
                    company = date.find('div', attrs={'class': 'title'}).find('a', attrs={'class': 'company'})
                    logo = date.find('div', attrs={'class': 'title'}).find('img', attrs={'class': 'f-i'})
                    jobs.append({
                        'title': title.text,
                        'url': href,
                        'description': content.text,
                        'company': company.text,
                        'logo': logo['src'] if logo else 'No logo',
                        'city_id': city, 'language_id': language,
                    })

            else:
                errors.append({
                    'url': url, 'title': 'Table does not exists'
                })
        else:
            errors.append({
                'url': url, 'title': 'Page do not response'
            })
    return jobs, errors












