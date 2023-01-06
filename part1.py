import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x * 2
print(y)
def graph1():
    plt.xlabel('X label')
    plt.ylabel('Y label')
    plt.title("Title of the graph")
    plt.plot(x,y)
    plt.show()
    print("Graph1")

def subgraph():
    #subplot
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(y, x, 'r')
    axes[1].plot(y, x, 'b')
    plt.show()

def graph2():
    #use by object
    fig = plt.figure()
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    #axes.plot(x, y)
    plt.show()

def graph3():
    fig = plt.figure()
    axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
    axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

    axes1.plot(x,y)
    axes1.set_title("Big graph")
    axes2.plot(y,x)
    axes2.set_title("Small graph")

    plt.show()







#graph1()
#subgraph()
#graph2()
graph3()