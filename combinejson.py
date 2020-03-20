import json

if __name__ == "__main__":

    # just for testing purposes to truncate json file and make sure it starts out with correct formatting
    with open('allJsonAppendedTogether.json', 'w') as fp:
        #fp.truncate(0)
        # json.dump({"rows":[]}, fp)
        fp.write("{\"employees\":[]}")

    with open('allJsonAppendedTogether.json', 'r+') as fp:
        information = json.load(fp)

    pgNum = 1
    for fileRange in range(1, 3):
        with open('pg' + str(fileRange) + '.json', 'r') as jsonStr:
            jsonStrText = json.load(jsonStr, strict=False)
        for index, item in enumerate(jsonStrText['rows']):
            itemNum = item['cell']
            item['id'] = pgNum * 20 + int(item['id']) - 20
            item['year'] = itemNum[1]
            item['location'] = itemNum[2]
            for character in itemNum[3]:
                if character == " ":
                    itemNum3 = itemNum[3].split(" ", 1)
                    item['firstName'] = itemNum3[0].title()
                    #print(item['firstName'])
                    item['middleName(s)'] = itemNum3[1].title()
                    #print(item['middleName(s)'])
                    break
                else:
                    item['firstName'] = itemNum[3].title()
                    item['middleName(s)'] = ''
            item['lastName'] = itemNum[4].title()
            item['title'] = itemNum[5]
            item['grossPay'] = itemNum[6]
            item['regularPay'] = itemNum[7]
            item['overtimePay'] = itemNum[8]
            item['otherPay'] = itemNum[9]
            item.pop('cell')
            rowInfo = jsonStrText["rows"][index]
            information["employees"].append(rowInfo)
        pgNum += 1

    #print(information)

    with open('allJsonAppendedTogether.json', 'w') as fp:
        json.dump(information, fp, indent = 1)







    """with open('allJsonAppendedTogether.json', 'r+') as obj:
    

        data = json.load(obj)
        print(data['rows'][1])"""



    #TODO:
    # 1. Make a new file that is for combining all the json stuff
    # 2. Open pg1 and extract data from pg1 to new file
    # 3. Open pg2
    # 4. Make ID unique by a math calculation: pgNum * 10 + id
    # 5. Append contents of pg 2 to new file
    # 6. Loop 3-5
