import json
import requests
import sqlite3
import time
"where testid='1'"
db_url='project/test.db'
sql_execute="SELECT testid, pcount  from people_count "
josn_url='D:/apache-tomcat-9.0.37/webapps/Fire/a123.json'

def main():
    conn = sqlite3.connect(db_url)
    c = conn.cursor()

    c.execute(sql_execute)
    before=c.fetchall()

    while True:
        time.sleep(5)
        c.execute(sql_execute)
        after=c.fetchall()

        if len(after)<len(before):
            before=after
            continue
        change=after[len(before):]
        #读json
        with open(josn_url, "r",encoding='utf-8') as jsonFile:
            data = json.load(jsonFile)
        #修改数据
        if len(change)!=0:
            data=[]
        for row in change:
            print("Changed:ID = ", row[0], "    count = ", row[1])
            data.append({'id':row[0],'count':row[1]})   
        #写json
        with open(josn_url, "w") as jsonFile:
            json.dump(data, jsonFile,ensure_ascii=False)

        before=after
    conn.close()
    
if __name__ == "__main__":
    main()