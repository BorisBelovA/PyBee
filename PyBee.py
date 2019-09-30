import random
from collections import OrderedDict

scouts = 10
bestSectorsBees = 5
choosenSectorsBees = 2
bestSectorsAmount = 2
bestSectors = []
choosenSectorsAmount = 3
choosenSectors = []
sectorRange = 2

sectors = {}

def f(x, y):
    return x ** 2 + y ** 2

def fillBestAndChoosenSectors():
    # Сортировка сектрово по значению функции
    sortedSectors = sorted(sectors.keys())
    for i in sortedSectors:
        if len(bestSectors) <= bestSectorsAmount - 1:
            bestSectors.append(sectors[i])
        elif len(choosenSectors) <= choosenSectorsAmount - 1:
            choosenSectors.append(sectors[i])
    #print('bestSectors',bestSectors)

def getNewSectors():
    new_sectors = {}
    print('bs',bestSectors)
    print('cs',choosenSectors)
    for i in bestSectors:
        new_sectors[f(i[0], i[1])] = i
        x_range = [i[0] - sectorRange, i[0] + sectorRange]
        y_range = [i[1] - sectorRange, i[1] + sectorRange]
        for bBee in range(bestSectorsBees-1):
            x_new = random.randint(x_range[0], x_range[1])
            y_new = random.randint(y_range[0], y_range[1])
            new_sectors[f(x_new, y_new)] = [x_new, y_new]
            # ПОчему то не значения иногда увеличиваются
    for i in choosenSectors:
        new_sectors[f(i[0], i[1])] = i
        x_range = [i[0] - sectorRange, i[0] + sectorRange]
        y_range = [i[1] - sectorRange, i[1] + sectorRange]
        for bBee in range(choosenSectorsBees-1):
            x_new = random.randint(x_range[0], x_range[1])
            y_new = random.randint(y_range[0], y_range[1])
            new_sectors[f(x_new, y_new)] = [x_new, y_new]
    print('New',new_sectors)
    return new_sectors

def makeIteration(sectors):
    print('Sectors', sectors)
    bestSectors = []
    choosenSectors = []
    fillBestAndChoosenSectors()
    return  getNewSectors()




for _ in range(10):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    sectors[f(x, y)] = [x, y]


# Заполняем массив с лучшими и выбранными секторами
#fillBestAndChoosenSectors()

# Из лучших и выбранных секторов получили список новый значений
#sectors = getNewSectors()
#print(sectors)

#Начало новой итерации

sectors = makeIteration(sectors)

print('Sorted',sorted(sectors.keys()))

sectors = makeIteration(sectors)
print('Sorted',sorted(sectors.keys()))

sectors = makeIteration(sectors)
print('Sorted',sorted(sectors.keys()))

sectors = makeIteration(sectors)
print('Sorted',sorted(sectors.keys()))

sectors = makeIteration(sectors)
print('Sorted',sorted(sectors.keys()))

sectors = makeIteration(sectors)
print('Sorted',sorted(sectors.keys()))

