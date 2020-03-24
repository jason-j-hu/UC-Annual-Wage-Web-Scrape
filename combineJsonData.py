import json


def setup_file(new_file_name):
    with open(new_file_name + ".json", 'w') as fp:
        fp.truncate(0)
        fp.write("{\"employees\":[]}")


def func(new_file_name, original_file_path):
    with open(new_file_name + '.json', 'r+') as fp:
        information = json.load(fp)

    with open(original_file_path + "/pg1.json", 'r') as fp:
        max_pgs = int(json.load(fp)['total'])

    for fileRange in range(1, max_pgs+1): #15515+1
        with open(original_file_path + '/pg' + str(fileRange) + '.json', 'r') as json_fp:
            json_string = json.load(json_fp, strict=False)
        for index, item in enumerate(json_string['rows']):
            item_num = item['cell']
            item['year'] = item_num[1]
            item['location'] = item_num[2]
            for character in item_num[3]:
                if character == " ":
                    item_num_temp = item_num[3].split(" ", 1)
                    item['firstName'] = item_num_temp[0].title()
                    item['middleName(s)'] = item_num_temp[1].title()
                    break
                else:
                    item['firstName'] = item_num[3].title()
                    item['middleName(s)'] = ''
            item['lastName'] = item_num[4].title()
            item['title'] = item_num[5]
            item['grossPay'] = item_num[6]
            item['regularPay'] = item_num[7]
            item['overtimePay'] = item_num[8]
            item['otherPay'] = item_num[9]
            item.pop('id')
            item.pop('cell')
            rowInfo = json_string["rows"][index]
            information["employees"].append(rowInfo)

    with open(new_file_name + '.json', 'w') as fp:
        json.dump(information, fp, indent=1)

if __name__ == "__main__":
    setup_file("allJsonAppendedTogether")
    for yr in range(2010, 2018+1):
        func("allJsonAppendedTogether", f'./{yr}/ALL')
        print(f"Year {yr} Data Combined")
