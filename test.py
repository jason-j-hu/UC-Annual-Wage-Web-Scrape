import requests
import ast
import json

# from bs4 import BeautifulSoup

# TODO:
# 1. Convert all single quotes to double quotes in r.text
# 2. Use json.load to find ['total'] key and use it in range()
# 3. Use for loop to download all the pages of data into seperate .json files
# 4. Merge the json files into one using the ID thing and page
# 5. Make everything into functions
# 6.

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

    pgNum = 1
    while True:

        payload['page'] = pgNum
        r = requests.get(url, params=payload)
        rTextFixedDoubleQuote = r.text.replace("\'", "\"")
        rTextJson = json.loads(rTextFixedDoubleQuote)

        obj = open("pg" + str(pgNum) + ".json", "w")

        obj.write(rTextFixedDoubleQuote)

        if pgNum == 5:  # rTextJson['total']
            break
        pgNum += 1


    """
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
    # print(ast.literal_eval(r.text))
    totalPgs = int(ast.literal_eval(r.text)['total'])



    obj.close()
    """
