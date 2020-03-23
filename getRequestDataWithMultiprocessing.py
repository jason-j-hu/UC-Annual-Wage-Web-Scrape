import requests
from multiprocessing.pool import ThreadPool
import re
import os
import ast
from time import time


def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


@run_once
def create_dir(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
    except:
        pass


def download_json(url):
    regex_split = re.split('&|=', url)
    pg_num = regex_split[7]
    yr_num = regex_split[13]
    loc_val = regex_split[15]
    folder_path = f"./{yr_num}/{loc_val}"
    create_dir(folder_path)

    if os.path.isfile(f"{folder_path}/pg{pg_num}.json"):
        print("pg" + pg_num + " data skipped\n")
    else:
        print("pg" + pg_num + " data collected\n")
        r = requests.get(url)
        r.raise_for_status()
        r_text_fixed = r.text.replace("\'", "\"")
        with open(f"{folder_path}/pg{pg_num}.json", "x") as obj:
            obj.write(r_text_fixed)


def get_urls(list, yr_num, loc_val, row_num):
    sample_url = f"https://ucannualwage.ucop.edu/wage/search.action?_search=false&nd=1584252598793&rows={row_num}&page=1&sidx=EAW_GRS_EARN_AMT&sord=desc&year={yr_num}&location={loc_val}&firstname=&lastname=&title=&startSal=&endSal="
    r = requests.get(sample_url)
    last_pg = int(ast.literal_eval(r.text)['total'])
    if last_pg == 0:
        last_pg += 1
    for pg_num in range(1, last_pg + 1):
        list.append(
            f"https://ucannualwage.ucop.edu/wage/search.action?_search=false&nd=1584252598793&rows={row_num}&page={pg_num}&sidx=EAW_GRS_EARN_AMT&sord=desc&year={yr_num}&location={loc_val}&firstname=&lastname=&title=&startSal=&endSal=")


def check_quit(prompt):
    if prompt in ('Q', 'q'):
        exit()

def get_valid_int(prompt, param):
    while True:
        try:
            int_val = input(prompt)
            check_quit(int_val)
            int_val = int(int_val)
        except ValueError:
            print("Please input an integer.\n")
            continue

        if param == 'year':
            if not 2010 <= int_val <= 2018:
                print("Selected year must be between 2010 to 2018.\n")
                continue
            else:
                break
        elif param == 'rows':
            if not 1 <= int_val <= 999999999:
                print("Each json file must contain at least 1 data row. The maximum data rows per json file is 999,999,999. \n")
                continue
            else:
                break
    return int_val


def get_valid_loc(prompt):
    while True:
        loc = input(prompt)
        check_quit(loc)
        if not loc in ('ASUCLA', 'Berkeley', 'Davis', 'Hastings', 'Irvine', 'Los Angeles', 'Merced', 'Riverside', 'San Diego', 'San Francisco', 'Santa Barbara', 'Santa Cruz', 'UCOP', 'ALL'):
            print("Selected location must be of the following options (case-sensitive): ASUCLA, Berkeley, Davis, Hastings, Irvine, Los Angeles, Merced, Riverside, San Diego, San Francisco, Santa Barbara, Santa Cruz, UCOP, ALL.\n")
            continue
        else:
            break
    return loc


if __name__ == '__main__':
    print("Hello! This python script downloads University of California employee pay data in aggregate. Input \'Q\' or \'q\' at any time to quit the script during the input phase.")
    year = get_valid_int("What calendar year would you like to download? ", 'year')
    location = get_valid_loc("What location would you like to download? ")
    rows = get_valid_int("How many data rows would you like per json file? ", 'rows')

    print("Thank you for your input! (script made by Jason Hu)\n********\nDATA GENERATING...")
    start = time()

    urls_list = []
    get_urls(urls_list, year, location, rows)

    results = ThreadPool(6).imap_unordered(download_json, urls_list)

    for r in results:
        pass

    print(f"Time to download: {time() - start}")
