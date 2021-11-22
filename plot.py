import matplotlib.pyplot as plt
from random import randint

NUMOFBARS = 100
MINVALUE = 0
MAXVALUE = 100

def createPlot(x, y):
    plt.bar(x,y)
    plt.show()
    plt.clf()

def getAxisValues():
    x = []
    y = []
    for i in range(NUMOFBARS):
        x.append(i)
        y.append(randint(MINVALUE,MAXVALUE))
    return x,y

def easySort(x):
    return x.sort()

def main():
    x,y = getAxisValues()
    createPlot(x,y)
    #newX = easySort(x)
    createPlot(x.sort(),y)

if __name__ == '__main__':
    main()