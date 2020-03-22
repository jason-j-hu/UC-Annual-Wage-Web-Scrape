from time import time
start = time()
import requests
import json
from multiprocessing.pool import ThreadPool


def download_json(url):
    r = requests.get(url, stream=True)
    r_text_fixed = r.text.replace("\'", "\"")

    r_text_json = json.loads(r_text_fixed)
    pg_num = r_text_json['page']

    with open(f"rawDataTest/pg{pg_num}.json", "x") as obj:
        obj.write(r_text_fixed)


if __name__ == '__main__':
    urlsList = []
    for pgNum in range(1, 30):
        url = "https://ucannualwage.ucop.edu/wage/search.action"
        payload = {'_search': 'false',
                   'nd': 1584252598793,
                   'rows': 20,
                   'page': pgNum,
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
        urlsList.append(r.url)
    print(urlsList)
    results = ThreadPool(5).imap_unordered(download_json, urlsList)
    for r in results:
        pass
    print(f"Time to download: {time() - start}")