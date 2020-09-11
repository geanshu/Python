import json
import requests
import sqlite3
import time

def main():
    conn = sqlite3.connect('project/test.db')
    c = conn.cursor()

    c.execute("SELECT testid, pcount  from people_count where testid='1' ")
    before=c.fetchall()

    while True:
        time.sleep(5)
        c.execute("SELECT testid, pcount  from people_count where testid='1' ")
        after=c.fetchall()

        if len(after)<len(before):
            continue
        change=after[len(before):]
        #读json
        with open("project/a123.json", "r",encoding='utf-8') as jsonFile:
            data = json.load(jsonFile)
        #修改数据
        for row in change:
            print("Changed:ID = ", row[0], "    count = ", row[1])
            data.append({'id':row[0],'count':row[1]})   
        #写json
        with open("project/a123.json", "w") as jsonFile:
            json.dump(data, jsonFile,ensure_ascii=False)

        before=after
    conn.close()
    
if __name__ == "__main__":
    main()