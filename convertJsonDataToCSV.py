import json
import csv


if __name__ == "__main__":
    with open('allJsonAppendedTogether.json', 'r') as fp:
        data = json.load(fp)['employees']

    with open('allJsonAppendedTogether.csv', 'w') as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)
