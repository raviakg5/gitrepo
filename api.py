import requests

import dbhelper
from dbconnection import Dbconnection
from dbhelper import DBHelper
from query import sql
conn = Dbconnection().get_connection_db()

try:
    #cursor = conn.cursor()
    response = requests.get('https://randomuser.me/api')

    print(response.status_code)
    gender = response.json()['results'][0]['gender']
    print(gender)

    title = response.json()['results'][0]['name']['title']


    first = response.json()['results'][0]['name']['first']

    last = response.json()['results'][0]['name']['last']

    print(title+' '+first+' '+last)
    val = (title+' '+first, last,gender)
    print(sql)
    print(val)
    DBHelper().executedbsqlquery(sql.format(first,last,gender))

    #sql = "INSERT INTO user.example ( FirstName,LastName,Gender) VALUES (%s, %s,%s)"



except Exception as e:
    print(f'database connectivity error {e}')

