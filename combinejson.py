import json

if __name__ == "__main__":

    obj = open('allJsonAppendedTogether.json', 'r+')
    a = json.load(obj)
    print(a)
    b = a['rows']
    print(b)
    b.append("hello")
    print(b)

    """with open('pg1.json', 'r') as jsonStr:
        jsonStrText = json.load(jsonStr)
        for idIndex in range(0, 20):
            rowInfo = jsonStrText['rows'][idIndex]
            print(rowInfo)
            json.dump(rowInfo, obj)"""

    """with open('allJsonAppendedTogether.json', 'r+') as obj:
    

        data = json.load(obj)
        print(data['rows'][1])"""




    """
        pgNum = 2
    
        while pgNum <= 5:
            with open('pg' + str(pgNum) + '.json', 'r') as jsonStr:
                jsonStrText = json.load(jsonStr)
                for dataRow in jsonStrText['rows']:
                    dataRow['id'] = pgNum * 10 + int(dataRow['id'])
                    # TODO: append data rows to the allJsonAppendedTogether.json file
            pgNum += 1"""
    obj.close()
    #TODO:
    # 1. Make a new file that is for combining all the json stuff
    # 2. Open pg1 and extract data from pg1 to new file
    # 3. Open pg2
    # 4. Make ID unique by a math calculation: pgNum * 10 + id
    # 5. Append contents of pg 2 to new file
    # 6. Loop 3-5
