import csv
import matplotlib.pyplot as plt

f = open('age11_21.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
old = []
old_tmp = 0
for row in data :
    for i in range(16, 24) :
        old_tmp += int(row[i])
    old.append(((old_tmp) / int(row[0])) * 100)
    old_tmp = 0
        
plt.title('gangseo 65-100+ rate graph')
plt.plot(old, 'green', label = '65-100+')
plt.legend()
plt.show()