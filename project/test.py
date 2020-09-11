import json
import requests
import sqlite3
import time

def main():
    conn = sqlite3.connect('project/test.db')
    c = conn.cursor()
    print("Opened database successfully")
    c.execute("SELECT testid, pcount  from people_count where testid='4' ")
    before=c.fetchall()

    while True:
        time.sleep(1)
        c.execute("SELECT testid, pcount  from people_count where testid='4' ")
        after=c.fetchall()
        if len(after<before):
            continue
        change=after[len(before):]

        for row in change:
            print("Changed:ID = ", row[0], "    count = ", row[1])

            requests.post(url='http://localhost:8080/Fire/', data=json.dumps({
                'id': row[0],
                'count': row[1]
            }), headers={'content_type': 'application/json'})
        before=after
    conn.close()

if __name__ == "__main__":
    main()