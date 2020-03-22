import requests
from multiprocessing.pool import ThreadPool
# import multiprocessing
import re
import os
import ast
from time import time
start = time()


def download_json(url, path = 2017):
    """
    r_text_json = json.loads(r_text_fixed)
    pg_num = r_text_json['page']
    """
    pg_num = re.findall(r'\d+', url)[2]
    if not os.path.isfile(f"{path}/pg{pg_num}.json"):
        print("pg" + pg_num + " data collected\n")
        r = requests.get(url)
        r.raise_for_status()
        r_text_fixed = r.text.replace("\'", "\"")
        with open(f"{path}/pg{pg_num}.json", "x") as obj:
            obj.write(r_text_fixed)
    else:
        print("pg" + pg_num + " data skipped\n")


def get_urls(list, row_num, yr_num):
    sample_url = f"https://ucannualwage.ucop.edu/wage/search.action?_search=false&nd=1584252598793&rows={row_num}&page=1&sidx=EAW_GRS_EARN_AMT&sord=desc&year={yr_num}&location=ALL&firstname=&lastname=&title=&startSal=&endSal="
    r = requests.get(sample_url)
    last_pg = int(ast.literal_eval(r.text)['total'])

    for pg_num in range(1, last_pg+1):
        list.append(f"https://ucannualwage.ucop.edu/wage/search.action?_search=false&nd=1584252598793&rows={row_num}&page={pg_num}&sidx=EAW_GRS_EARN_AMT&sord=desc&year={yr_num}&location=ALL&firstname=&lastname=&title=&startSal=&endSal=")


if __name__ == '__main__':
    urls_list = []
    get_urls(urls_list, 2000, 2017)

    """
    p = multiprocessing.Pool(2)
    results = p.imap_unordered(download_json, urls_list)
    """
    results = ThreadPool(6).imap_unordered(download_json, urls_list)

    for r in results:
        pass
    print(f"Time to download: {time() - start}")
