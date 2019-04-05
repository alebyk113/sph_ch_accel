import os
import pandas as pd
import json


class Load_data:
	def __init__(self, data_path, meta_path):
		self.data_path = data_path

		self.file_list = [f for f in os.listdir(self.data_path) if not f.startswith('.')]    
		self.acceleration_keys = json.load(open(os.path.join(meta_path, 'accelerometer_axes.json')))
		self.rssi_keys = json.load(open(os.path.join(meta_path, 'access_point_names.json')))

	def load_accel(self):

		dfs = []

		for fi, file_id in enumerate(self.file_list):
			f_name = os.path.join(self.data_path,file_id,'acceleration.csv')
			accel_rssi = pd.read_csv(f_name, index_col=0)

			accel = accel_rssi[self.acceleration_keys]

			dfs.append(accel)

		return dfs











