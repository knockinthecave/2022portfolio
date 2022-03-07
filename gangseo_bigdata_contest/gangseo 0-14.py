import csv
import matplotlib.pyplot as plt

f = open('age11_21.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
kids = []

for row in data :
    kids.append((int(row[2])+int(row[3])+int(row[4]) / int(row[0]))*100)

plt.title('gangseo 0-14 rate graph')
plt.plot(kids, 'red', label = '0-14')
plt.legend()
plt.show()
