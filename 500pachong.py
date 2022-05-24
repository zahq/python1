# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='lottery', charset='utf8')

    cursor = conn.cursor()

    target = 'https://trade.500.com/jczq/'
    req = requests.get(url=target)
    print(req.encoding)  # gbk
    html = req.text.encode('gbk')
    bf = BeautifulSoup(html, features='html.parser')
    texts = bf.find_all('table', class_='bet-tb bet-tb-dg')
    bf1 = BeautifulSoup(str(texts[1]), features='html.parser')
    bf2 = bf1.find_all('tr', class_='bet-tb-tr')
    for each in bf2:
        bf3 = BeautifulSoup(str(each), features='html.parser')
        bf4 = bf3.find_all('p', class_='betbtn')
        bf5 = BeautifulSoup(str(bf4[0]), features='html.parser')
        bf6 = bf5.find_all('span')
        for each1 in bf6:
            print(each.get('data-homesxname'), each1.string)
            sql2 = "insert into lottery0501 (name,date01,date02,date03,date04,result) values ('%s','%s',''," \
                   "'','','')" % (each.get('data-homesxname'), each1.string)
            cursor.execute(sql2)

        # 提交事务:
    conn.commit()
    cursor.close()
