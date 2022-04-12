import csv
from openpyxl import Workbook

f = open('Yeongdeungpo_take.csv', 'r', encoding='utf-8')
data = csv.reader(f)

y2014q1_jumpo = 0
y2014q1_gain = 0
y2014q2_jumpo = 0
y2014q2_gain = 0
y2014q3_jumpo = 0
y2014q3_gain = 0
y2014q4_jumpo = 0
y2014q4_gain = 0

y2015q1_jumpo = 0
y2015q1_gain = 0
y2015q2_jumpo = 0
y2015q2_gain = 0
y2015q3_jumpo = 0
y2015q3_gain = 0
y2015q4_jumpo = 0
y2015q4_gain = 0

y2016q1_jumpo = 0
y2016q1_gain = 0
y2016q2_jumpo = 0
y2016q2_gain = 0
y2016q3_jumpo = 0
y2016q3_gain = 0
y2016q4_jumpo = 0
y2016q4_gain = 0

y2017q1_jumpo = 0
y2017q1_gain = 0
y2017q2_jumpo = 0
y2017q2_gain = 0
y2017q3_jumpo = 0
y2017q3_gain = 0
y2017q4_jumpo = 0
y2017q4_gain = 0

y2018q1_jumpo = 0
y2018q1_gain = 0
y2018q2_jumpo = 0
y2018q2_gain = 0
y2018q3_jumpo = 0
y2018q3_gain = 0
y2018q4_jumpo = 0
y2018q4_gain = 0

y2019q1_jumpo = 0
y2019q1_gain = 0
y2019q2_jumpo = 0
y2019q2_gain = 0
y2019q3_jumpo = 0
y2019q3_gain = 0
y2019q4_jumpo = 0
y2019q4_gain = 0

y2020q1_jumpo = 0
y2020q1_gain = 0
y2020q2_jumpo = 0
y2020q2_gain = 0
y2020q3_jumpo = 0
y2020q3_gain = 0
y2020q4_jumpo = 0
y2020q4_gain = 0

next(data)
for row in data :
    if int(row[1]) == 2014 :
        if int(row[2]) == 1 :
            y2014q1_jumpo += int(row[7])
            y2014q1_gain += int(row[6])
        elif int(row[2]) == 2 :
            y2014q2_jumpo += int(row[7])
            y2014q2_gain += int(row[6])
        elif int(row[2]) == 3 :
            y2014q3_jumpo += int(row[7])
            y2014q3_gain += int(row[6])
        elif int(row[2]) == 4 :
            y2014q4_jumpo += int(row[7])
            y2014q4_gain += int(row[6])
    
    elif int(row[1]) == 2015 :
        if int(row[2]) == 1 :
            y2015q1_jumpo += int(row[7])
            y2015q1_gain += int(row[6])
        elif int(row[2]) == 2 :
            y2015q2_jumpo += int(row[7])
            y2015q2_gain += int(row[6])
        elif int(row[2]) == 3 :
            y2015q3_jumpo += int(row[7])
            y2015q3_gain += int(row[6])
        elif int(row[2]) == 4 :
            y2015q4_jumpo += int(row[7])
            y2015q4_gain += int(row[6]) 
    
    elif int(row[1]) == 2016 :
        if int(row[2]) == 1 :
            y2016q1_jumpo += int(row[7])
            y2016q1_gain += int(row[6])
        elif int(row[2]) == 2 :
            y2016q2_jumpo += int(row[7])
            y2016q2_gain += int(row[6])
        elif int(row[2]) == 3 :
            y2016q3_jumpo += int(row[7])
            y2016q3_gain += int(row[6])
        elif int(row[2]) == 4 :
            y2016q4_jumpo += int(row[7])
            y2016q4_gain += int(row[6]) 
    
    elif int(row[1]) == 2017 :
        if int(row[2]) == 1 :
            y2017q1_jumpo += int(row[7])
            y2017q1_gain += int(row[6])
        elif int(row[2]) == 2 :
            y2017q2_jumpo += int(row[7])
            y2017q2_gain += int(row[6])
        elif int(row[2]) == 3 :
            y2017q3_jumpo += int(row[7])
            y2017q3_gain += int(row[6])
        elif int(row[2]) == 4 :
            y2017q4_jumpo += int(row[7])
            y2017q4_gain += int(row[6])  
    
    elif int(row[1]) == 2018 :
        if int(row[2]) == 1 :
            y2018q1_jumpo += int(row[7])
            y2018q1_gain += int(row[6])
        elif int(row[2]) == 2 :
            y2018q2_jumpo += int(row[7])
            y2018q2_gain += int(row[6])
        elif int(row[2]) == 3 :
            y2018q3_jumpo += int(row[7])
            y2018q3_gain += int(row[6])
        elif int(row[2]) == 4 :
            y2018q4_jumpo += int(row[7])
            y2018q4_gain += int(row[6]) 

    elif int(row[1]) == 2019 :
        if int(row[2]) == 1 :
            y2019q1_jumpo += int(row[7])
            y2019q1_gain += int(row[6])
        elif int(row[2]) == 2 :
            y2019q2_jumpo += int(row[7])
            y2019q2_gain += int(row[6])
        elif int(row[2]) == 3 :
            y2019q3_jumpo += int(row[7])
            y2019q3_gain += int(row[6])
        elif int(row[2]) == 4 :
            y2019q4_jumpo += int(row[7])
            y2019q4_gain += int(row[6]) 
    
    elif int(row[1]) == 2020 :
        if int(row[2]) == 1 :
            y2020q1_jumpo += int(row[7])
            y2020q1_gain += int(row[6])
        elif int(row[2]) == 2 :
            y2020q2_jumpo += int(row[7])
            y2020q2_gain += int(row[6])
        elif int(row[2]) == 3 :
            y2020q3_jumpo += int(row[7])
            y2020q3_gain += int(row[6])
        elif int(row[2]) == 4 :
            y2020q4_jumpo += int(row[7])
            y2020q4_gain += int(row[6]) 

w2014 = 0.942
w2015 = 0.949
w2016 = 0.958
w2017 = 0.976
w2018 = 0.991
w2019 = 0.995
w2020 = 1

av_y14q1 = (((y2014q1_gain) * w2014) / 10000) / (y2014q1_jumpo)
av_y14q2 = (((y2014q2_gain) * w2014) / 10000) / (y2014q2_jumpo)
av_y14q3 = (((y2014q3_gain) * w2014) / 10000) / (y2014q3_jumpo)
av_y14q4 = (((y2014q4_gain) * w2014) / 10000) / (y2014q4_jumpo)

av_y15q1 = (((y2015q1_gain) * w2015) / 10000) / (y2015q1_jumpo)
av_y15q2 = (((y2015q2_gain) * w2015) / 10000) / (y2015q2_jumpo)
av_y15q3 = (((y2015q3_gain) * w2015) / 10000) / (y2015q3_jumpo)
av_y15q4 = (((y2015q4_gain) * w2015) / 10000) / (y2015q4_jumpo)

av_y16q1 = (((y2016q1_gain) * w2016) / 10000) / (y2016q1_jumpo)
av_y16q2 = (((y2016q2_gain) * w2016) / 10000) / (y2016q2_jumpo)
av_y16q3 = (((y2016q3_gain) * w2016) / 10000) / (y2016q3_jumpo)
av_y16q4 = (((y2016q4_gain) * w2016) / 10000) / (y2016q4_jumpo)

av_y17q1 = (((y2017q1_gain) * w2017) / 10000) / (y2017q1_jumpo)
av_y17q2 = (((y2017q2_gain) * w2017) / 10000) / (y2017q2_jumpo)
av_y17q3 = (((y2017q3_gain) * w2017) / 10000) / (y2017q3_jumpo)
av_y17q4 = (((y2017q4_gain) * w2017) / 10000) / (y2017q4_jumpo)

av_y18q1 = (((y2018q1_gain) * w2018) / 10000) / (y2018q1_jumpo)
av_y18q2 = (((y2018q2_gain) * w2018) / 10000) / (y2018q2_jumpo)
av_y18q3 = (((y2018q3_gain) * w2018) / 10000) / (y2018q3_jumpo)
av_y18q4 = (((y2018q4_gain) * w2018) / 10000) / (y2018q4_jumpo)

av_y19q1 = (((y2019q1_gain) * w2019) / 10000) / (y2019q1_jumpo)
av_y19q2 = (((y2019q2_gain) * w2019) / 10000) / (y2019q2_jumpo)
av_y19q3 = (((y2019q3_gain) * w2019) / 10000) / (y2019q3_jumpo)
av_y19q4 = (((y2019q4_gain) * w2019) / 10000) / (y2019q4_jumpo)

av_y20q1 = (((y2020q1_gain) * w2020) / 10000) / (y2020q1_jumpo)
av_y20q2 = (((y2020q2_gain) * w2020) / 10000) / (y2020q2_jumpo)
av_y20q3 = (((y2020q3_gain) * w2020) / 10000) / (y2020q3_jumpo)
av_y20q4 = (((y2020q4_gain) * w2020) / 10000) / (y2020q4_jumpo)

x = ['2014_1', '2014_2', '2014_3', '2014_4', 
'2015_1', '2015_2', '2015_3', '2015_4',
'2016_1', '2016_2', '2016_3', '2016_4',
'2017_1', '2017_2', '2017_3', '2017_4',
'2018_1', '2018_2', '2018_3', '2018_4',
'2019_1', '2019_2', '2019_3', '2019_4',
'2020_1', '2020_2', '2020_3', '2020_4']

jumpo_list = [y2014q1_jumpo, y2014q2_jumpo, y2014q3_jumpo, y2014q4_jumpo,
y2015q1_jumpo, y2015q2_jumpo, y2015q3_jumpo, y2015q4_jumpo,
y2016q1_jumpo, y2016q2_jumpo, y2016q3_jumpo, y2016q4_jumpo,
y2017q1_jumpo, y2017q2_jumpo, y2017q3_jumpo, y2017q4_jumpo,
y2018q1_jumpo, y2018q2_jumpo, y2018q3_jumpo, y2018q4_jumpo,
y2019q1_jumpo, y2019q2_jumpo, y2019q3_jumpo, y2019q4_jumpo,
y2020q1_jumpo, y2020q2_jumpo, y2020q3_jumpo, y2020q4_jumpo]

av_list = [av_y14q1, av_y14q2, av_y14q3, av_y14q4,
av_y15q1, av_y15q2, av_y15q3, av_y15q4,
av_y16q1, av_y16q2, av_y16q3, av_y16q4,
av_y17q1, av_y17q2, av_y17q3, av_y17q4, 
av_y18q1, av_y18q2, av_y18q3, av_y18q4,
av_y19q1, av_y19q2, av_y19q3, av_y19q4, 
av_y20q1, av_y20q2, av_y20q3, av_y20q4]

write_wb = Workbook()
write_ws = write_wb.active
write_ws.append(x)
write_ws.append(jumpo_list)
write_ws.append(av_list)
write_wb.save("Yeongdeungpo_data.xlsx")









