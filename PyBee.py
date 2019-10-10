import random
import time
from collections import OrderedDict
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Фитнесс-функция
def f(x, y, z):
    return x ** 2 + y ** 2 + z ** 2


# Заполнение лучших и выбранных секторов
def fillBestAndChoosenSectors(sectors, bestSectorsAmount, choosenSectorsAmount):
    # Сортировка сектрово по значению функции
    bestSectors = []
    choosenSectors = []
    sortedSectors = sorted(sectors.keys())
    for i in sortedSectors:
        if len(bestSectors) <= bestSectorsAmount - 1:
            bestSectors.append(sectors[i])
        elif len(choosenSectors) <= choosenSectorsAmount - 1:
            choosenSectors.append(sectors[i])
    return [bestSectors, choosenSectors]


# Определение новых секторов на основе лучших и выбранных
def getNewSectors(bestSectors, bestSectorsBees, choosenSectors, choosenSectorsBees, sectorRange):
    new_sectors = {}
    for i in bestSectors:
        new_sectors[f(i[0], i[1], i[2])] = i
        x_range = [i[0] - sectorRange, i[0] + sectorRange]
        y_range = [i[1] - sectorRange, i[1] + sectorRange]
        z_range = [i[2] - sectorRange, i[2] + sectorRange]
        for bBee in range(bestSectorsBees - 1):
            x_new = random.uniform(x_range[0], x_range[1])
            y_new = random.uniform(y_range[0], y_range[1])
            z_new = random.uniform(z_range[0], z_range[1])
            new_sectors[f(x_new, y_new, z_new)] = [x_new, y_new, z_new]
            # ПОчему то не значения иногда увеличиваются
    for i in choosenSectors:
        new_sectors[f(i[0], i[1], i[2])] = i
        x_range = [i[0] - sectorRange, i[0] + sectorRange]
        y_range = [i[1] - sectorRange, i[1] + sectorRange]
        z_range = [i[2] - sectorRange, i[2] + sectorRange]
        for bBee in range(choosenSectorsBees - 1):
            x_new = random.uniform(x_range[0], x_range[1])
            y_new = random.uniform(y_range[0], y_range[1])
            z_new = random.uniform(z_range[0], z_range[1])
            new_sectors[f(x_new, y_new, z_new)] = [x_new, y_new, z_new]
    return new_sectors


# Начальная инициализация секторов
def initSectors(scouts):
    sectors = {}
    for _ in range(scouts):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        z = random.uniform(-100, 100)
        sectors[f(x, y, z)] = [x, y, z]
    return sectors


def getExpectedValue(arrayOfValues):
    print(arrayOfValues)

def plotDots(sectors):
    ax = plt.axes(projection='3d')

    for s in sectors:
        # print(sectors[s])
        ax.scatter(sectors[s][0], sectors[s][1], sectors[s][2])
    ax.margins(0, 0, 0)
    plt.show()

def main():
    scouts = 15

    # Кол-во пчел, отправляемых на лучшие сектора
    bestSectorsBees = 10

    # Кол-во пчел, отправляемых на выбранные участки
    choosenSectorsBees = 5

    # Кол-во лучших участков
    bestSectorsAmount = 3

    # Кол-во выбранных участков
    choosenSectorsAmount = 5

    # Размер сектора
    sectorRange = 10

    sectors = initSectors(scouts)
    i = 0

    # print('best', f(*sectors[sorted(sectors.keys())[0]]))
    currentBestSolution = f(*sectors[sorted(sectors.keys())[0]])
    prevBestSolution = f(*sectors[sorted(sectors.keys())[2]])

    def makeIteration(sectors):
        # print('initial sectors: \n', sectors)

        bestSectors, choosenSectors = fillBestAndChoosenSectors(sectors, bestSectorsAmount, choosenSectorsAmount)

        # print('best sectors: \n', bestSectors)
        # print('chosen sectors: \n', choosenSectors)

        new_sectors = getNewSectors(bestSectors, bestSectorsBees, choosenSectors, choosenSectorsBees, sectorRange)

        # print('new sectors: \n', new_sectors)
        return new_sectors

    # Критерий останова - i-я итерация
    repeatedCounter = 0
    GLOBAL_MIN = 0
    M = 0
    #while currentBestSolution != GLOBAL_MIN:
    #while repeatedCounter < 40:
    while i < 10000:
        prevBestSolution = currentBestSolution
        temp = makeIteration(sectors)
        sectors = temp
        currentBestSolution = f(*sectors[sorted(sectors.keys())[0]])
        #print(prevBestSolution,currentBestSolution)
        M+=currentBestSolution
        if (prevBestSolution == currentBestSolution):
            repeatedCounter += 1
        else:
            repeatedCounter = 0
        if(i%10 == 0):
            print('Итерация ', i , ' --- ', currentBestSolution)
        i += 1
    #print("M", M/i)
    # Взять значение функции на каждой итерации
    # Подсчитать кол-во повторений кадого значения
    # M = (n0 * f(x0,y0,z0) + .... + ni * f(xi,yi,zi))/ N
    print('Минимум функции в точке: ', sectors[currentBestSolution], currentBestSolution)
    return sectors


#sectors = main()

#plotDots(sectors)

#plt.ion()
axes = plt.gca()
axes.set_xlim(-2,2)
axes.set_ylim(-2,2)
for i in range(10):
    y = np.random.random([10,1])
    plt.plot(y, 'ro')
    plt.draw()
    plt.pause(0.1)
    plt.clf()
plt.show()
#print('Сектора', sectors)


# for i in range(100):
#     t0 = time.time()
#     res = main()
#     t1 = time.time()
#     print(i,' - ', res, ' time - ', t1-t0)

