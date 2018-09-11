import requests
import json
import pymysql

class SeoulAppDB :
    def __init__(self, _host, _user, _password, _db):
        self.conn = pymysql.connect(
            host=_host,
            user=_user,
            password=_password,
            db=_db,
            charset='utf8'
        )
        self.db = self.conn.cursor()

    def insert(self, data):
        before = "SELECT * FROM `servicies` WHERE SVCID='%s'" % (data['SVCID'])
        self.db.execute(before)

        isExist = self.db.fetchone()

        sql = ''

        if isExist :
            sql = "UPDATE `servicies` SET" \
                  "`SVCID`='%s', " \
                  "`SVCNM`='%s', " \
                  "`PAYATNM`='%s', " \
                  "`MAXCLASSNM`='%s', " \
                  "`MINCLASSNM`='%s', " \
                  "`AREANM`='%s', " \
                  "`PLACENM`='%s', " \
                  "`SVCSTATNM`='%s', " \
                  "`USETGTINFO`='%s', " \
                  "`X`='%f', " \
                  "`Y`='%f', " \
                  "`SVCOPNBGNDT`='%s', " \
                  "`SVCOPNENDDT`='%s', " \
                  "`SVCURL` = '%s'" \
                  "WHERE `SVCID`='"+ data['SVCID'] +"';"
        else :
            sql = "INSERT INTO `servicies`(" \
                  "`SVCID`, " \
                  "`SVCNM`, " \
                  "`PAYATNM`, " \
                  "`MAXCLASSNM`, " \
                  "`MINCLASSNM`, " \
                  "`AREANM`, " \
                  "`PLACENM`, " \
                  "`SVCSTATNM`, " \
                  "`USETGTINFO`, " \
                  "`X`, " \
                  "`Y`, " \
                  "`SVCOPNBGNDT`, " \
                  "`SVCOPNENDDT`," \
                  "`SVCURL`)" \
                  "VALUES ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %f, %f, '%s', '%s', '%s');"

        sql = sql % (
            data['SVCID'],
            data['SVCNM'].replace("'", '"'),
            data['PAYATNM'].replace("'", '"'),
            data['MAXCLASSNM'],
            data['MINCLASSNM'],
            data['AREANM'],
            data['PLACENM'].replace("'", '"'),
            data['SVCSTATNM'],
            data['USETGTINFO'].replace("'", '"'),
            float(data['X'] + '0'),
            float(data['Y'] + '0'),
            data['SVCOPNBGNDT'],
            data['SVCOPNENDDT'],
            data['SVCURL'],
        )

        self.db.execute(sql)

    def __del__(self):
        self.conn.commit()
        self.conn.close()

DB = SeoulAppDB('localhost', 'cho8wola', '462719', 'seoulapp')

services = [
    'Sport',
    'Education',
    'Institution',
    'Culture',
    'Medical',
]


for service in services:
    SVCSTR = 'ListPublicReservation' + service

    for i in range(0, 10, 1):
        PARSE_URL = u"http://openapi.seoul.go.kr:8088/414f414a6963686f33316d65547677/json/"+SVCSTR+"/"+ str((i*500)+1) +"/" + str((i+1)*500)
        res = requests.get(PARSE_URL)
        JSON_DATA = json.loads(res.text)

        print(PARSE_URL)

        if SVCSTR in JSON_DATA:
            data = JSON_DATA[SVCSTR]['row']

            #pprint.pprint(data)

            for d in data:
                DB.insert(d)