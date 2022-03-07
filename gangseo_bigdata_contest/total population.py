import csv
import matplotlib.pyplot as plt

f = open('age11_21.csv', 'r', encoding='cp949')
data = csv.reader(f)
next(data)
total = []

for row in data :
    total.append(int(row[0]))

plt.title("gangseo's total population")
plt.plot(total, 'red', label='total')
plt.legend()
plt.show()



