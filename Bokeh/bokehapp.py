<<<<<<< HEAD
# imports

from bokeh.plotting import figure
from bokeh.io import output_notebook, show, push_notebook

from bokeh.plotting import ColumnDataSource
from bokeh.layouts import row, column

from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

import numpy as np
import pandas as pd


#-----------------------

# Create ColumnDataSource: source
N=300
source = ColumnDataSource(data={'x':np.random.random(N),
                                'y':np.random.random(N)})
# 300 random numbers from 0 to 1

# Add a line to the plot
plot=figure()
plot.circle(x='x', y='y', source=source)

# add a slider
slider = Slider(start=100,end=1000,value=N,step=10,title='Number of Points')

# Define a callback function: callback
def callback(attr, old, new): #always this way

    # Read the current value of the slider: scale
    scale = slider.value

    # Update source with the new data values
    source.data = {'x': np.random.random(scale), 
                   'y': np.random.random(scale)}

# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create a column layout: layout
layout = column(widgetbox(slider), plot) # the silder that is created 2 exercises ago
# calling the eidgetbox first in column to make sure slider is above plot

=======
# imports

from bokeh.plotting import figure
from bokeh.io import output_notebook, show, push_notebook

from bokeh.plotting import ColumnDataSource
from bokeh.layouts import row, column

from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models import Slider

import numpy as np
import pandas as pd


#-----------------------

# Create ColumnDataSource: source
N=300
source = ColumnDataSource(data={'x':np.random.random(N),
                                'y':np.random.random(N)})
# 300 random numbers from 0 to 1

# Add a line to the plot
plot=figure()
plot.circle(x='x', y='y', source=source)

# add a slider
slider = Slider(start=100,end=1000,value=N,step=10,title='Number of Points')

# Define a callback function: callback
def callback(attr, old, new): #always this way

    # Read the current value of the slider: scale
    scale = slider.value

    # Update source with the new data values
    source.data = {'x': np.random.random(scale), 
                   'y': np.random.random(scale)}

# Attach the callback to the 'value' property of slider
slider.on_change('value',callback)

# Create a column layout: layout
layout = column(widgetbox(slider), plot) # the silder that is created 2 exercises ago
# calling the eidgetbox first in column to make sure slider is above plot

>>>>>>> connect commit
curdoc().add_root(layout)