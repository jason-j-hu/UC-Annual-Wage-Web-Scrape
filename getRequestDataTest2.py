from time import time
start = time()
import requests
import json
from multiprocessing import Pool


def download_json(url):
    r = requests.get(url)
    r_text_fixed = r.text.replace("\'", "\"")

    r_text_json = json.loads(r_text_fixed)
    pg_num = r_text_json['page']

    with open(f"rawDataTest/pg{pg_num}.json", "x") as obj:
        obj.write(r_text_fixed)


def get_urls(pg_num):
    url = "https://ucannualwage.ucop.edu/wage/search.action"
    payload = {'_search': 'false',
               'nd': 1584252598793,
               'rows': 20,
               'page': pg_num,
               'sidx': 'EAW_GRS_EARN_AMT',
               'sord': 'desc',
               'year': 2018,
               'location': 'ALL',
               'firstname': '',
               'lastname': '',
               'title': '',
               'startSal': '',
               'endSal': ''}
    r = requests.get(url, params=payload)
    return r.url

if __name__ == '__main__':
    p = Pool(15)

    urls_list = []
    results_test = p.imap_unordered(get_urls, range(1, 30))
    for r in results_test:
        urls_list.append(r)
    print(urls_list)

    results = p.imap_unordered(download_json, urls_list)
    for r in results:
        pass
    print(f"Time to download: {time() - start}")