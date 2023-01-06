import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,5,11)
y = x * 2


""" 
#print the 9 graph
fig, axes = plt.subplots(nrows=3,ncols=3)
plt.tight_layout()
plt.show()"""

"""#print the 2 graph
fig, axes1 = plt.subplots(nrows=1,ncols=2)
for ax in axes1:
    ax.plot(x,y)
plt.show()"""

"""fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.plot(y,x)
plt.show()
"""

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label = 'A Squard')
ax.plot(x,x**3,label = 'X Cubed')
ax.legend()
plt.show()