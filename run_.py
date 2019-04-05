from load_data import *
from feature_ext_ import *

data_path = './public_data/train'
meta_path = './public_data/metadata'


data = Load_data(data_path,meta_path)
dfs = data.load_accel()


f_e = Feature_extraction(data_path,dfs)


f_e.get_features(time_window=100)









