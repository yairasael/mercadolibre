import csv
import os
from db.mongodb import mongoDB

def main():
    toDB = []
    try:
        dir = os.getcwd()
        file = open(dir + '/UploadDB.csv')
        cvsFile = csv.reader(file, delimiter=',')
        next(cvsFile, None)
        for line in cvsFile:
            obj = {'name': line[0], 'cost': int(line[1])}
            toDB.append(obj)
    except ValueError as err:
        print(err)
    finally:
        insertDb(toDB)

def insertDb(data):
    try:
        db = mongoDB.db['cost']
        if db is not None:
            valInsert = db.insert_many(data)
            print(valInsert)
        else:
            print("not db")
    except ValueError as err:
        print(err)
    finally:
        return True
    
    

if __name__ == '__main__':
    main()