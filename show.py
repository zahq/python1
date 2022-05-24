import numpy as np
import matplotlib.pyplot as plt

import pymysql
from random import randint

plt.rcParams['font.sans-serif'] = ['KaiTi']

# change root password to yours:
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='lottery')

# 运行查询:
cursor = conn.cursor()
cursor.execute('SELECT id,NAME,date01 FROM lottery0503 ORDER BY NAME, id ASC')
values = cursor.fetchall()
# print(values)
temp1 = 0
x1 = 0
a = []
b = []
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
markers = ['s', 'p', 'v', 'o', 'd', 'h', 'x']
for each1 in values:
    for index in range(len(each1)):
        print("index:", index, "value:", each1[index])
        temp = each1[0]

    if (temp > temp1):
        temp1 = temp
        print("index:", temp1)
        name = each1[1]
        # print("name:", name)
        x1 = x1 + 1
        a.append(x1)
        b.append(float(each1[2]))  # float 是纵坐标排序
    else:
        print("idx:", temp)
        temp1 = temp
        # name = each1[1]
        # print("name:", name)

        c = randint(0, 6)
        d = randint(0, 6)
        plt.plot(a, b, markers[d] + '-', color=colors[c], label=name)  # s-   方形
        x1 = 0
        a.clear()
        b.clear()
        x1 = x1 + 1
        a.append(x1)
        b.append(float(each1[2]))

plt.xlabel('时间')
plt.ylabel('赔率')
plt.title("数据走势")
plt.legend()
plt.show()

# 关闭Cursor和Connection:
cursor.close()
conn.close()
