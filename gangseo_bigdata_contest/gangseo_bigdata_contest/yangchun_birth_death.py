import csv
import matplotlib.pyplot as plt

f = open('14_20_yangchun_birth.csv', 'r', encoding = 'utf-8')
data = csv.reader(f)

birth_death_diff = []
for row in data :
    birth_death_diff.append((int(row[2])) - (int(row[3])))

plt.title('yangchun (birth) - (death)')
plt.plot(birth_death_diff, 'red', label = '(birth) - (death)')
plt.legend()
plt.show()