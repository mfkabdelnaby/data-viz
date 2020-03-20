# bokehapp.py

from bokeh.plotting import figure
from bokeh.io import output_notebook, show, push_notebook

from bokeh.plotting import ColumnDataSource
from bokeh.layouts import row, column

from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider,Select

from numpy.random import random, normal, lognormal
import pandas as pd


#-----------------------
# Create ColumnDataSource: source
N=300
source = ColumnDataSource(data={'x':random(N),
                                'y':random(N)})
# 300 random numbers from 0 to 1

# Add a line to the plot
plot=figure()
plot.circle(x='x', y='y', source=source)

# add a slider
menu = Select(options=['unifrom','normal','lognormal'],value='uniform', title='Distribution')
# value = current selection from the menu (in options)

# Define a callback function: callback
def callback(attr, old, new): #always this way
    
    if menu.value == 'uniform':   f = random
    elif menu.value ==  'normal': f = normal
    else:                         f = lognormal
    source.data={'x':f(size=N),'y':f(size=N)}
menu.on_change('value',callback)

# Create a column layout: layout
layout = column(menu, plot) # the silder that is created 2 exercises ago
# calling the eidgetbox first in column to make sure slider is above plot

curdoc().add_root(layout)