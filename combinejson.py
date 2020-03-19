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
    for fileRange in range(1, 10):
        with open('pg' + str(fileRange) + '.json', 'r') as jsonStr:
            jsonStrText = json.load(jsonStr, strict=False)
        for index, item in enumerate(jsonStrText['rows']):
            item['id'] = pgNum * 20 + int(item['id']) - 20
            rowInfo = jsonStrText["rows"][index]
            information["employees"].append(rowInfo)
        pgNum += 1

    #print(information)

    with open('allJsonAppendedTogether.json', 'w') as fp:
        json.dump(information, fp, indent=3)


    """pgNum = 1

    while pgNum <= 5:
        with open('pg' + str(pgNum) + '.json', 'r') as jsonStr:
            jsonStrText = json.load(jsonStr)
            print(jsonStrText['rows'][1])
            for dataRow in jsonStrText['rows']:
                dataRow['id'] = pgNum * 20 + int(dataRow['id']) - 20
            #print(dataRow)
                # TODO: append data rows to the allJsonAppendedTogether.json file
        pgNum += 1"""




    """with open('pg1.json', 'r') as jsonStr:
        jsonStrText = json.load(jsonStr)
    for idIndex in range(0, 20):
        rowInfo = jsonStrText['rows'][idIndex]
        print(rowInfo)"""




    """obj = open('allJsonAppendedTogether.json', 'r+')
    mergedFile = json.load(obj)
    b = print(mergedFile)
    mergedFile['rows'].append("hello")
    print(mergedFile['rows'])
    json.dump(b, obj)"""



    """with open('allJsonAppendedTogether.json', 'r+') as obj:
    

        data = json.load(obj)
        print(data['rows'][1])"""





    #obj.close()

    #TODO:
    # 1. Make a new file that is for combining all the json stuff
    # 2. Open pg1 and extract data from pg1 to new file
    # 3. Open pg2
    # 4. Make ID unique by a math calculation: pgNum * 10 + id
    # 5. Append contents of pg 2 to new file
    # 6. Loop 3-5
