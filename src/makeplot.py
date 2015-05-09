from matplotlib import pylab
from matplotlib.ticker import ScalarFormatter

import numpy
import seaborn
seaborn.set(style="white", context="talk")
time = numpy.array([571, 229, 165, 7.31, 39.6, 5.61, 6.75])
labels= numpy.array([
    'Python', 'def() naive', 'def() typed', 'cdef()', 'cpdef()', 'cpdef typed', 'C'])
hlines=numpy.arange(1, 10)
axes = seaborn.barplot(y=time, x=labels, x_order=labels)
axes.yaxis.label.set_text("Time (ms)")
axes.yaxis.grid(color='black', which='both')
axes.set_yscale('log')
axes.set_ylim(1, 1000)
axes.yaxis.set_major_formatter(ScalarFormatter())
pylab.show()
