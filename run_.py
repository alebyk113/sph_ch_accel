from load_data import *
from feature_ext_ import *
import numpy as np


data_path = './public_data/train'
meta_path = './public_data/metadata'


data = Load_data(data_path,meta_path)
dfs = data.load_accel()


f_e = Feature_extraction(data_path,dfs)


fxn_list = [np.mean,np.median]



f_e.get_features(time_window=1000,fxn_list=fxn_list)









