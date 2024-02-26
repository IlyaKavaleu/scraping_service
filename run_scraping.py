import asyncio
import codecs
import json
import sys
import os
import django
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import DatabaseError
import datetime as dt


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'

django.setup()

from scraping.parsers import *
from scraping.models import Vacancy, Language, City, Error, Url

User = get_user_model()

parsers = (
    (work, 'work'),
    (dou, 'dou'),
    (jooble, 'jooble'),
    (ria, 'ria'),
    (work_java, 'work_java'),
    (dou_java, 'dou_java'),
    (jooble_java, 'jooble_java'),
    (ria_java, 'ria_java'),
    (work_c_plus_plus, 'work_c_plus_plus'),
    (dou_c_plus_plus, 'dou_c_plus_plus'),
    (jooble_c_plus_plus, 'jooble_c_plus_plus'),
    (ria_c_plus_plus, 'ria_c_plus_plus'),

    (jooble_python_gdansk, 'jooble_python_gdansk'),
    (dou_python_gdansk, 'dou_python_gdansk'),

    (jooble_java_gdansk, 'jooble_java_gdansk'),
    (dou_java_gdansk, 'dou_java_gdansk'),

    (dou_c_plus_plus_gdansk, 'dou_c_plus_plus_gdansk'),
    (jooble_c_plus_plus_gdansk, 'jooble_c_plus_plus_gdansk'),
)

jobs, errors = [], []


def get_settings():
    qs = User.objects.filter(send_email=True).values()
    settings_lst = set((q['city_id'], q['language_id']) for q in qs)
    return settings_lst


def get_urls(_settings):
    qs = Url.objects.all().values()
    url_dict = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        if pair in url_dict:
            tmp = {}
            tmp['city'] = pair[0]
            tmp['language'] = pair[1]
            url_data = url_dict.get(pair)
            if url_data:
                tmp['url_data'] = url_dict.get(pair)
                urls.append(tmp)
    return urls


async def main(value):
    func, url, city, language = value
    loop = asyncio.get_running_loop()
    job, err = await loop.run_in_executor(None, func, url, city, language)
    errors.extend(err)
    jobs.extend(job)

settings = get_settings()
url_list = get_urls(settings)
loop = asyncio.get_event_loop()

tmp_tasks = [(func, data['url_data'][key], data['city'], data['language'])
             for data in url_list
             for func, key in parsers]

# for data in url_list:
#     for func, key in parsers:
#         url = data['url_data'][key]
#         j, e = func(url, city=data['city'], language=data['language'])
#         jobs += j
#         errors += e

if tmp_tasks:
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])
    loop.run_until_complete(tasks)
    loop.close()

for job in jobs:
    v = Vacancy(
        **job,
    )
    try:
        v.save()
    except DatabaseError:
        pass

if errors:
    qs = Error.objects.filter(timestamp=dt.date.today())
    if qs.exists():
        err = qs.first()
        err.data.update({'errors': errors})
        err.save()
    else:
        er = Error(data=f'errors:{errors}').save()
print(jobs)
print('')

# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()
ten_days_ago = dt.date.today() - dt.timedelta(10)
Vacancy.objects.filter(timestamp__lte=ten_days_ago).delete()



