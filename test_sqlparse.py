#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlparse

sql = '''

   select avg(`timespan`) AS `avg`
   from `hive.dw`.`dw_netperformancelogs`



'''

sqlformat = sqlparse.format(sql, reindent=True, keyword_case='upper').split('\n')
for line in sqlformat:
    # if line!='':
    print line
