import matplotlib       # Provides the graph figures
matplotlib.use('WXAgg') # matplotlib needs a GUI (layout), we use wxPython
 
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas

# This times fires every 100 ms to redraw the graphs
self.redrawTimer = wx.Timer(self)
self.Bind(wx.EVT_TIMER, self.onRedrawTimer, self.redrawTimer)
self.redrawTimer.Start(500)

