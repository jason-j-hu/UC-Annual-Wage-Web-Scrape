import requests
url = "https://ucannualwage.ucop.edu/wage/search.action?_search=false&nd=1584252598793&rows=20&page=1&sidx=EAW_GRS_EARN_AMT&sord=desc&year=2018&location=Berkeley&firstname=&lastname=&title=&startSal=&endSal="

r = requests.get(url)
print(r.text)
r_text_fixed = r.text.replace("\'", "\"")


x = open('./2018/Berkeley/pg1.json').read()
print(x)
string = r_text_fixed

if requests.get(url).text.replace("\'", "\"") == open('./2018/Berkeley/pg1.json').read():
    print('Success')
else:
    print('Fail')




"""


r = requests.get(url)
r.raise_for_status()
r_text_fixed = r.text.replace("\'", "\"")
if os.path.isfile(f"{folder_path}/pg{pg_num}.json"):
    if r_text_fixed == open(f"{folder_path}/pg{pg_num}.json").read():
        open(f"{folder_path}/pg{pg_num}.json").close()
        print("pg" + pg_num + " data skipped\n")
    else:
        with open(f"{folder_path}/pg{pg_num}.json", "w") as obj:
            obj.write(r_text_fixed)
        print("pg" + pg_num + "data overwritten\n")
else:
    with open(f"{folder_path}/pg{pg_num}.json", "x") as obj:
        obj.write(r_text_fixed)
    print("pg" + pg_num + " data collected\n")

"""