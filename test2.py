import requests
import ast
import json

# from bs4 import BeautifulSoup



if __name__ == '__main__':
    url = "https://ucannualwage.ucop.edu/wage/search.action"
    payload = {'_search': 'false',
               'nd': 1584252598793,
               'rows': 20,
               'page': 1,
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
    print(r.url)
    payload['rows'] = ast.literal_eval(r.text)['records']
    r = requests.get(url, params=payload)
    obj = open("2017.json", "w")
    rTextFixedDoubleQuote = r.text.replace("\'", "\"")
    obj.write(rTextFixedDoubleQuote)
    obj.close()


