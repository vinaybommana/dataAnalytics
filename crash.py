import csv
import matplotlib.pyplot as plot

hours = []
Hours = []
Minutes =[]

for row in csv.reader(open('test.csv')):
    if row[1] != 'Time' and row[1] != '' :
        hours.append(row[1])

#print(hours)
#assert("False")
for i in hours:
    #print(i)
    try:
        H, M = i.split(":")
    except:
        try:
            H, M = i.split("'")
        except:
            try:
                c, H, M = i.split(":")
            except:
                try:
                    H, M = i.split(".")
                except:
                    pass
    Hours.append(H)
    Minutes.append(M)

#print(Hours)

OneCount = 0
TwoCount = 0
ThreeCount = 0
FourCount = 0
FiveCount = 0
SixCount = 0
SevenCount = 0
EightCount = 0
NineCount = 0
TenCount = 0
ElevenCount = 0
TwelveCount = 0
ThirteenCount = 0
FourteenCount = 0
FifteenCount = 0
SixteenCount = 0
SeventeenCount = 0
EighteenCount = 0
NineteenCount = 0
TwentyCount = 0
TwentyOneCount = 0
TwentyTwoCount = 0
TwentyThreeCount = 0
TwentyFourCount = 0

for i in Hours:
    if len(i) == 2:
        if i == '00':
            TwentyFourCount += 1
        elif i == '01':
            OneCount += 1
        elif i == '02':
            TwoCount += 1
        elif i == '03':
            ThreeCount += 1
        elif i == '04':
            FourCount += 1
        elif i == '05':
            FiveCount += 1
        elif i == '06':
            SixCount += 1
        elif i == '07':
            SevenCount += 1
        elif i == '08':
            EightCount += 1
        elif i == '09':
            NineCount += 1
        elif i == '10':
            TenCount += 1
        elif i == '11':
            ElevenCount += 1
        elif i == '12':
            TwelveCount += 1
        elif i == '13':
            ThirteenCount += 1
        elif i == '14':
            FourteenCount += 1
        elif i == '15':
            FifteenCount += 1
        elif i == '16':
            SixteenCount += 1
        elif i == '17':
            SeventeenCount += 1
        elif i == '18':
            EighteenCount += 1
        elif i == '19':
            NineteenCount += 1
        elif i == '20':
            TwentyCount += 1
        elif i == '21':
            TwentyOneCount += 1
        elif i == '22':
            TwentyTwoCount += 1
        elif i == '23':
            TwentyThreeCount += 1

xAxis = [i for i in range(24)]
yAxis = [TwentyFourCount,OneCount,TwoCount,ThreeCount,FourCount,FiveCount,SixCount,SevenCount,EightCount,NineCount,TenCount,ElevenCount,TwelveCount,ThirteenCount,FourteenCount,FifteenCount,SixteenCount,SeventeenCount,EighteenCount,NineteenCount,TwentyCount,TwentyOneCount,TwentyTwoCount,TwentyThreeCount]

#print(xAxis)

plot.bar(xAxis, yAxis, label='crashes', color='#006666')
plot.xlabel('Hour of Crash')
plot.ylabel('Number of Crashes')
plot.title('Hour of Crash vs Number of Crashes')
plot.legend()
plot.show()
