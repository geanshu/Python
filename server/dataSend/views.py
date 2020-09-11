import json
import sqlite3
from django.http import HttpResponse

conn = sqlite3.connect('./test.db')
c = conn.cursor()
c.execute("SELECT testid, pcount  from people_count where testid='1' ")
before = c.fetchall()
after=c.fetchall()
conn.close()

def getChange():
    conn = sqlite3.connect('./test.db')
    c = conn.cursor()
    c.execute("SELECT testid, pcount  from people_count where testid='1' ")
    after = c.fetchall()
    print(before)
    print(after)
    conn.close()
    if len(after) < len(before):
        return []
    change = after[len(before):]
    after=before
    return change

def getdata(request):
    data = []
    if request.method == 'GET':
        changeData=getChange()
        print('change',changeData)
        if len(changeData)==0:
            return HttpResponse(json.dumps(data))
        for row in changeData:
            data.append({'id':row[0],'count':row[1]})
    return HttpResponse(json.dumps(data))

