import csv
import matplotlib.pyplot as plt

f = open('age11_21.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
nor = []
nor_tmp = 0
for row in data :
    for i in range(5, 15) :
        nor_tmp += int(row[i])
    nor.append(((nor_tmp) / int(row[0])) * 100)
    nor_tmp = 0
        
plt.title('gangseo 15-64 rate graph')
plt.plot(nor, 'blue', label = '15-64')
plt.legend()
plt.show()