import numpy as np
import matplotlib.pyplot as plot

plot.rcParams.update({'font.size': 6})
yAxis = ('Aero Commander', 'Air bus', 'Antonov', 'Aveo', 'BAC', 'BAE', 'Beech', 'Bell', 'Boeing', 'Bristol', 'British AeroSpace', 'Britten-Norman', 'Canadair', 'Casa', 'Cenna', 'Consolidated', 'Convoir', 'Curtiss', 'de Havilland', 'Dornier', 'Douglas', 'Embrair', 'Fair child', 'Farman', 'Fokker', 'Ford', 'Grumman', 'Handles', 'Hawker', 'Ilycestin', 'Junkers', 'LateCoer', 'Lear jet', 'Let', 'Lockhead', 'McDohnell', 'Mil MI', 'Picatrue', 'Piper', 'RockWell', 'Shorts', 'Sikorksy', 'Strison', 'Sud-Aviation', 'Swearingen', 'Suffoleu', 'Vickern', 'Zeffenlin' )
#print(len(yAxis))
xAxis = [47, 37, 247, 48, 18, 9, 163, 64, 375, 26, 17, 86, 19, 38, 289, 43, 86, 134, 309, 18, 979, 61, 81, 11, 132, 27, 26, 22, 38, 100, 84, 18, 50, 39, 337, 126, 34, 12, 128, 9, 53, 51, 14, 23, 32, 95, 95, 16]
#print(len(xAxis))
y_pos = np.arange(len(yAxis))
plot.barh(y_pos, xAxis, align='center')
plot.yticks(y_pos, yAxis)
plot.title('Operator vs Crashes')
plot.xlabel('Crashes')
plot.ylabel('Operator')
plot.show()
