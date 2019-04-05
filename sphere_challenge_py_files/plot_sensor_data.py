from __future__ import print_function

# For number crunching
import numpy as np
import pandas as pd

# For visualisation
import matplotlib.pyplot as pl 
import seaborn as sns 

# For prediction 
import sklearn

# Misc
from itertools import cycle
import json 
import os
import sys

from visualise_data import SequenceVisualisation

sns.set_context('poster')
sns.set_style('darkgrid')
current_palette = cycle(sns.color_palette())


nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)

public_data_path = './public_data'
metadata_path = './public_data/metadata'
 

plotter = SequenceVisualisation(metadata_path, public_data_path + '/train/00001')
sequence_window = (plotter.meta['start'], plotter.meta['end'])


# plotter.plot_pir(sequence_window, sharey=True)
# plotter.plot_rssi(sequence_window)
# plotter.plot_acceleration((sequence_window[0] + 180, sequence_window[0] + 300))
# plotter.plot_video(plotter.centre_2d, sequence_window)
# pl.gcf().suptitle('2D bounding box')

# plotter.plot_video(plotter.centre_3d, sequence_window)
# pl.gcf().suptitle('3D bounding box')

# pl.show()


##### plot annotations

annotation_names = plotter.targets.columns.difference(['start', 'end'])

# Select only the first minute of data 
sub_df = plotter.targets.ix[:60 * 2]

# Select only the columns that are non-empty 
sub_df_cols = [col for col in annotation_names if sub_df[col].sum() > 0]

# Plot a bar-plot w
# sub_df[sub_df_cols].plot(
#     kind='bar', 
#     subplots=True, 
#     sharex=True, 
#     sharey=True, 
#     figsize=(20, 3 * len(sub_df_cols)), 
#     width=1.0, 
#     color=[next(current_palette) for _ in annotation_names]
# );















