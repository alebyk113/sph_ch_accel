"""
We will define two convenience function to load the extracted features and their 
"""
import pandas as pd
import numpy as np
import os
import json
from itertools import cycle
import seaborn as sns




def load_sequence(file_id):
    filename = str(file_id).zfill(5)

    df = pd.read_csv('{}/train/{}/columns_1000ms.csv'.format(public_data_path, filename))
    data = df.values
    target = np.asarray(pd.read_csv('{}/train/{}/targets.csv'.format(public_data_path, filename)))[:, 2:]

    return data, target


def load_sequences(file_ids):
    x_es = []
    y_es = []

    for file_id in file_ids:
        data, target = load_sequence(file_id)

        x_es.append(data)
        y_es.append(target)

    return np.row_stack(x_es), np.row_stack(y_es)


# Load the training and testing data 
public_data_path = './public_data'
metadata_path = './public_data/metadata'

train_x, train_y = load_sequences([1, 2, 3, 4, 5, 6, 7, 8])
test_x, test_y = load_sequences([9, 10])

print ("Check whether the train/test features are all finite (before imputation)")
print ('All training data finite:', np.all(np.isfinite(train_x)))
print ('All testing data finite:', np.all(np.isfinite(test_x)))


# We will want to impute the missing data 
from sklearn.preprocessing import Imputer
imputer = Imputer()
imputer.fit(train_x)

train_x = imputer.transform(train_x)
test_x = imputer.transform(test_x)

print ("Check whether the train/test features are all finite (after imputation)")
print ('All training data finite:', np.all(np.isfinite(train_x)))
print ('All testing data finite:', np.all(np.isfinite(test_x)))

# Load the label names 
labels = json.load(open(metadata_path + '/annotations.json'))
n_classes = len(labels)

"""
Note, not all data is annotated, so we select only the annotated rows
"""
train_y_has_annotation = np.isfinite(train_y.sum(1))
train_x = train_x[train_y_has_annotation]
train_y = train_y[train_y_has_annotation]

test_y_has_annotation = np.isfinite(test_y.sum(1))
test_x = test_x[test_y_has_annotation]
test_y = test_y[test_y_has_annotation]


"""
Print simple statistics regarding the number of instances
"""
print ("Training data shapes:")
print ("train_x.shape: {}".format(train_x.shape))
print ("train_y.shape: {}".format(train_y.shape))

print ("Testing data shapes")
print ("test_x.shape: {}".format(test_x.shape))
print ("test_y.shape: {}".format(test_y.shape))



activity_names = json.load(open(metadata_path + '/annotations.json', 'r'))
# class_weights = np.asarray(json.load(open(metadata_path + '/class_weights.json', 'r')))
class_weights = [1.35298455691, 1.38684574053, 1.59587388404, 1.35318713948, 0.347783666015, 0.661081706198, 1.04723628621, 0.398865222651, 0.207586320237, 1.50578335208, 0.110181365961, 1.07803284435, 1.36560417316, 1.17024113802, 1.1933637414, 1.1803704493, 1.34414875433, 1.11683830693, 1.08083910312, 0.503152249073]
class_prior = train_y.mean(0)

df = pd.DataFrame({
        'Activity': activity_names, 
        'Class Weight': class_weights,
        'Prior Class Distribution': class_prior
    })

df.set_index('Activity', inplace=True)
# reset colour palette
current_palette = cycle(sns.color_palette())
df.plot(
    kind='bar',
    width=1.0,
    subplots=True,
    color=[next(current_palette), next(current_palette)], 
)

print(df)
# train_y[10:20,:]









import json
from visualise_data import SequenceVisualisation
import os

class_prior = train_y.mean(0)

public_data_path = './public_data'
metadata_path = './public_data/metadata'

plotter = SequenceVisualisation(metadata_path, public_data_path + '/train/00001')
annotation_names = plotter.targets.columns.difference(['start', 'end'])

se_cols = ['start', 'end']

num_lines = 0

with open('submission_prior_baseline.csv', 'w') as fil: 
    fil.write(','.join(['record_id'] + se_cols + annotation_names.tolist()))
    fil.write('\n')
            
    for te_ind_str in sorted(os.listdir(os.path.join(public_data_path, 'test')))[1:]:

        te_ind = int(te_ind_str)

        meta = json.load(open(os.path.join(public_data_path, 'test', te_ind_str, 'meta.json')))

        starts = range(meta['end'])
        ends = range(1, meta['end'] + 1)

        for start, end in zip(starts, ends):
            row = [te_ind, start, end] + class_prior.tolist()

            fil.write(','.join(map(str, row)))
            fil.write('\n')
            
            num_lines += 1
            
print ("{} lines written.".format(num_lines))






















