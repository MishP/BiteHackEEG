__author__ = 'ivan'

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import matplotlib.pyplot as plt
import time
app = QtGui.QApplication([])



win = pg.GraphicsWindow(title="Real Time EEG")
win.setWindowTitle('Real Time EEG')
win.resize(1000, 600)
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="Alpha")
curve1 = p1.plot(pen='y')
data = np.random.normal(size=(10,100))
ptr = 0


p2 = win.addPlot(title="Beta")
curve2 = p2.plot(pen='y')


p3 = win.addPlot(title="Gamma")
curve3 = p3.plot(pen='y')
win.nextRow()

p4 = win.addPlot(title="Delta")
curve4 = p4.plot(pen='y')


p5 = win.addPlot(title="Theta")
curve5 = p5.plot(pen='y')


p6 = win.addPlot(title="Sigma")
curve6 = p6.plot(pen='y')
win.nextRow()

p7 = win.addPlot(title="Happy")
curve7 = p7.plot(pen='y')


p8 = win.addPlot(title="Excitement")
curve8 = p8.plot(pen='y')


p9 = win.addPlot(title="Concentration")
curve9 = p9.plot(pen='y')
win.nextRow()

def update():
    global curve1, curve2, curve3, curve4, curve5, curve6, curve7, curve8, curve9, data, ptr, p1
    curve1.setData(data[ptr%10])
    curve2.setData(data[ptr%10])
    curve3.setData(data[ptr%10])
    curve4.setData(data[ptr%10])
    curve5.setData(data[ptr%10])
    curve6.setData(data[ptr%10])
    curve7.setData(data[ptr%10])
    curve8.setData(data[ptr%10])
    curve9.setData(data[ptr%10])
    if ptr == 0:
        p1.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
    timer.start(1000)
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)






if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()



