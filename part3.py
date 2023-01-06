import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x * 2
def graph1():
    x = np.linspace(0,5,11)
    y = x * 2
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.plot(x,y,color = 'blue', lw = 1,ls = ':',marker = 'o', markersize = 2, markerfacecolor = 'yellow', markeredgecolor = 'green')
    plt.show()

def graph2():
    plt.scatter(x,y)
    plt.show()
#graph1()
graph2()
