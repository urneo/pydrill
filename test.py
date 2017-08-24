from pydrill.client import PyDrill
from pydrill.dbapi import drill

sql = '''
SELECT `timespan`, avg(`timespan`) AS `avg`
FROM `hive.dw`.`dw_netperformancelogs`
group by `timespan`
limit 1
'''
host, port = '192.168.0.3', 18047

db = PyDrill(host='192.168.0.3', port=18047)
db = drill.connect(host, port, catalog='hive', schema='dw')
cursor = db.cursor()
cursor.execute(sql)

# for row in cursor:
#     print row

print cursor.description
