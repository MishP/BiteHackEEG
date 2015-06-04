import matplotlib.pyplot as plt
import numpy as np
import time

fig = plt.figure()
ax = fig.add_subplot(111)

# some X and Y data
x = np.arange(1000)
y = np.random.randn(1000)
x2 = np.arange(1000)
y2 = np.random.randn(1000)


li, = ax.plot(x, y)
li2, =  ax.plot(x2, y2)


# draw and show it
fig.canvas.draw()
plt.show(block=False)

# loop to update the data
while True:
    try:
        y[:-10] = y[10:]
        y[-10:] = np.random.randn(10)

        # set the new data
        li.set_ydata(y)

        fig.canvas.draw()

        time.sleep(1)
    except KeyboardInterrupt:
        break