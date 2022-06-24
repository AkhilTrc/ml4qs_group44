import sys
sys.path.append('ML4QS-master')
%matplotlib inline

from Chapter2.CreateDataset import CreateDataset
import math
from util.VisualizeDataset import VisualizeDataset
from util import util
import copy
import os

import matplotlib
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [20,15]
matplotlib.rc('font', **{'family' : 'normal', 'size'   : 22})
matplotlib.rc('xtick',labelsize=22)
matplotlib.rc('ytick',labelsize=22)

DATA_PATH = './parkinson_dataset/csv/pre_arranged_data/'
RESULT_PATH = './parkinson_dataset/granularity_test'
granularities = [250, 500, 1000, 60000]

def roundup(x):
    return int(math.ceil(x))

for milliseconds_per_instance in granularities:
    
    print('For Granularity: ', milliseconds_per_instance)
        
    print('Creating empty dataset...')
    DataSet = CreateDataset(DATA_PATH, milliseconds_per_instance)

    print('Adding Numerical data...')
    DataSet.add_numerical_dataset(f'dataset_{name}.csv', 'timestamps', ['acc_x',
                                         'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z',
                                         'labelAtaxicGait', 'labelBradykinesia', 'labelFreezingOfGait',
                                         'labelMuscleAtrophy', 'labelMyopathicGait', 'labelNoPathologicalGait',
                                         'labelSittingWithTremor'], 'avg', '')

    # Get the resulting pandas data table.
    #
    print('Converting to pandas data table...')
    dataset = DataSet.data_table

    # fix labels when multiple labels in same row.
    #
    for x in dataset.columns:
        if 'label' in x:
            dataset[x] = dataset[x].apply(roundup)
                
    # Plot and Visualize.
    #
    DataViz = VisualizeDataset()
    DataViz.plot_dataset_boxplot(dataset, ['acc_x','acc_y','acc_z', 'gyr_x','gyr_y','gyr_z'])
    DataViz.plot_dataset(dataset, ['acc_x','acc_y','acc_z', 'gyr_x','gyr_y','gyr_z', 'label'], 
                                         ['like', 'like', 'like', 'like', 'like', 'like', 'like'], 
                                             ['line', 'line', 'line', 'line', 'line', 'line', 'points'])

    util.print_statistics(dataset)

dataset.to_csv(RESULT_PATH + f'granularities_{name}.csv')
print('Saved as csv!')

for key, value in data.items():
    name = key[8:]
    create_granularity(DATA_PATH, RESULT_PATH, granularities, name)