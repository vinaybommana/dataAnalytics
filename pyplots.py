import csv
import matplotlib.pyplot as plot

dates = []
fatalities_string = []
Aboard_string = []

for row in csv.reader(open('test.csv')):
    if row[0] != 'Date':
        dates.append(row[0])
    if row[10] != 'Fatalities':
        fatalities_string.append(row[10])
    if row[9] != 'Aboard':
        Aboard_string.append(row[9])


combined_list = []
for date in dates:
    combined_list.append(date.split('/'))

years = []
#print(years)
for year in combined_list:
    for i in year:
        if len(i) == 4:
            years.append(i)

fatalities = []
aboard = []
sum_of_fatalities = {}
aboard_and_year = {}
for i in fatalities_string:
    if i != '':
        fatalities.append(int(i))

for i in Aboard_string:
    if i != '':
        aboard.append(int(i))

i = iter(years)
j = iter(fatalities)
k = list(zip(i, j))

year = iter(years)
a = iter(aboard)
l = list(zip(year, a))
for (year, a) in l:
    if year in aboard_and_year:
        aboard_and_year[year] = aboard_and_year[year] + int(a)
    else:
        aboard_and_year[year] = int(a)

for (x, y) in k:
    if x in sum_of_fatalities:
        sum_of_fatalities[x] = sum_of_fatalities[x] + int(y)
    else:
        sum_of_fatalities[x] = int(y)

#print(sum_of_fatalities)
xAxis = list(sum_of_fatalities.keys())
xAxis = [int(i) for i in xAxis]
yAxis = list(sum_of_fatalities.values())
zAxis = list(aboard_and_year.values())
#print(xAxis)
#print(yAxis)
plot.bar(xAxis, zAxis, label='Aboard', color='#146de4')
plot.bar(xAxis, yAxis, label='Fatalities', color='#f45628')
plot.xlabel('Year')
plot.ylabel('Fatality')
plot.title('Years vs Fatalities')
plot.legend()
plot.show()
#print(aboard_and_year)
