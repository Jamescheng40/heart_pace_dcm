import matplotlib.pyplot as plt
import numpy as np
 
x = [0,1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
 
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'b-') 
 
for phase in range(10):
    y = [0,1,2,3,4,5,6,7,8,9]
    line1.set_ydata(y)
    y[2] = y[2] + phase
    fig.canvas.draw()
