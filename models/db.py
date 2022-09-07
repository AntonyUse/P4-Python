#!/usr/bin/python

import csv

# db = db.New('test.csv', ['id', 'name', 'age'])
# player1 = {'name':'John', 'age':45}
# player2 = {'name':'Robert', 'age':74}
# db.create([player1, player2])


# player3 = {'name':'Jean', 'age':37}
# player4 = {'name':'Anto', 'age':40}

# db.add([player3, player4])

# db.edit(player3)

class New():
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers
        # self.datas = []

    def create(self, datas):
        recDatas = []
        i = 0
        # print(datas)
        for row in datas:
            print(row)
            row['id'] = i
            recDatas.append(row)
            i += 1

        # print(recDatas)

        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(recDatas)

    def add(self, datas):
        recDatas = []
        myreader = csv.DictReader(open(self.filename, newline=''))

        i = len(list(myreader))
        for row in datas:
            row['id'] = i
            recDatas.append(row)
            i += 1

        # print(recDatas)

        with open(self.filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headers)
            writer.writerows(recDatas)

    def read(self):
        rows = []
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                rows.append(row)
        return rows

    def edit(self, newRow):
        filerows = self.read()
        # print(filerows)

        for row in filerows:
            # print(row)
            if (row['name'] == newRow['name']):
                row['age'] = newRow['age']
        # print(filerows)

        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(filerows)
