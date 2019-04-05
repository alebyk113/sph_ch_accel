from load_data import *
from feature_ext_ import *

data_path = './public_data/train'
meta_path = './public_data/metadata'


data = Load_data(data_path,meta_path)
df = data.load_accel()











