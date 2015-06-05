import matplotlib.pyplot as plt
import numpy as np
import time

fig = plt.figure()


ax = fig.add_subplot(1)
a2 = fig.add_subplot(2)


# some X and Y data
x = np.arange(100)
y = np.random.randn(100)

li, = ax.plot(x, y)
l2, = a2.plot(x+10, y+10)

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
        a2.set_ydata(y)


        fig.canvas.draw()

        time.sleep(0.01)
    except KeyboardInterrupt:
        break