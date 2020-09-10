import json
import requests
import sqlite3


conn = sqlite3.connect('project/test.db')
c = conn.cursor()
print("Opened database successfully")
cursor = c.execute("SELECT testid, pcount  from people_count")
for row in cursor:
    print("ID = ", row[0],"    count = ", row[1])

print("Operation done successfully")
conn.close()
# return HttpResponse(json.dumps{
#     'id': id,
#     'count': count
# }))
