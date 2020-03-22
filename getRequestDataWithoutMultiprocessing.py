import requests
import os.path

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

    for pgNum in range(1, 30): #15515+1
        if os.path.isfile(f"rawDataTest/pg{str(pgNum)}.json"):
            pass
        else:
            payload['page'] = pgNum
            r = requests.get(url, params=payload)
            rTextFixedDoubleQuote = r.text.replace("\'", "\"")

            obj = open(f"rawDataTest/pg{str(pgNum)}.json", "x")
            obj.write(rTextFixedDoubleQuote)
            obj.close()
