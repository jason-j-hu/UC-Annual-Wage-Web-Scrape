from time import time
start = time()
import requests
import multiprocessing
import re
import os

def download_json(url):
    r = requests.get(url)
    r.raise_for_status()
    r_text_fixed = r.text.replace("\'", "\"")

    pg_num = re.findall(r'\d+', url)[2]
    if not os.path.isfile(f"rawDataTest/pg{pg_num}.json"):
        with open(f"rawDataTest/pg{pg_num}.json", "x") as obj:
            obj.write(r_text_fixed)

def get_urls(list, first_pg, last_pg):
    for pg_num in range(first_pg, last_pg+1):
        list.append(f"https://ucannualwage.ucop.edu/wage/search.action?_search=false&nd=1584252598793&rows=20&page={pg_num}&sidx=EAW_GRS_EARN_AMT&sord=desc&year=2018&location=ALL&firstname=&lastname=&title=&startSal=&endSal=")

if __name__ == '__main__':
    urls_list = []
    get_urls(urls_list, 1, 15515)
    p = multiprocessing.Pool(2)
    print(multiprocessing.cpu_count())
    print(os.cpu_count())
    results = p.imap_unordered(download_json, urls_list)
    for r in results:
        pass
    print(f"Time to download: {time() - start}")
