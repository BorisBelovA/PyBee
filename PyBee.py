import random
from collections import OrderedDict

# Фитнесс-функция
def f(x, y):
    return x ** 2 + y ** 2

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
        new_sectors[f(i[0], i[1])] = i
        x_range = [i[0] - sectorRange, i[0] + sectorRange]
        y_range = [i[1] - sectorRange, i[1] + sectorRange]
        for bBee in range(bestSectorsBees - 1):
            x_new = random.randint(x_range[0], x_range[1])
            y_new = random.randint(y_range[0], y_range[1])
            new_sectors[f(x_new, y_new)] = [x_new, y_new]
            # ПОчему то не значения иногда увеличиваются
    for i in choosenSectors:
        new_sectors[f(i[0], i[1])] = i
        x_range = [i[0] - sectorRange, i[0] + sectorRange]
        y_range = [i[1] - sectorRange, i[1] + sectorRange]
        for bBee in range(choosenSectorsBees - 1):
            x_new = random.randint(x_range[0], x_range[1])
            y_new = random.randint(y_range[0], y_range[1])
            new_sectors[f(x_new, y_new)] = [x_new, y_new]
    return new_sectors

# Начальная инициализация секторов
def initSectors(scouts):
    sectors = {}
    for _ in range(scouts):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        sectors[f(x, y)] = [x, y]
    return sectors

def main():
    scouts = 10

    # Кол-во пчел, отправляемых на лучшие сектора
    bestSectorsBees = 5

    # Кол-во пчел, отправляемых на выбранные участки
    choosenSectorsBees = 2

    # Кол-во лучших участков
    bestSectorsAmount = 2

    # Кол-во выбранных участков
    choosenSectorsAmount = 3

    # Размер сектора
    sectorRange = 2

    sectors = initSectors(scouts)
    i = 0

    def makeIteration(sectors):
        print('initial sectors: \n', sectors)

        bestSectors, choosenSectors = fillBestAndChoosenSectors(sectors, bestSectorsAmount, choosenSectorsAmount)

        print('best sectors: \n', bestSectors)
        print('chosen sectors: \n', choosenSectors)

        new_sectors = getNewSectors(bestSectors, bestSectorsBees, choosenSectors, choosenSectorsBees, sectorRange)

        print('new sectors: \n', new_sectors)
        return new_sectors

    # Критерий останова - i-я итерация
    while i < 100:
        temp = makeIteration(sectors)
        sectors = temp
        i += 1

main()

# TODO: Перевести это все на функцию 3-х переменных
# TODO: Посмотреть что там по заданию с нескольких прогонами, замерами, матожиданием и дисперсией