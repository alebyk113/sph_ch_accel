import pandas as pd
import json
import os
import numpy as np

class Feature_extraction:
	def __init__(self,data_path, dfs):
		
		self.data_path = data_path
		self.dfs = dfs

		self.file_list = [f for f in os.listdir(self.data_path) if not f.startswith('.')]    
		self.n_files = len(self.file_list)

		self.ends=[]


		for fi, file_id in enumerate(self.file_list):
			self.meta = json.load(open(os.path.join(self.data_path,file_id, 'meta.json')))
			self.ends.append(self.meta['end'])
		


	def get_features(self,time_window,fxn_list):
		'''time_window in ms'''

		lower = np.arange(0,self.ends[0],time_window)
		upper = np.arange(time_window,self.ends[0]+time_window,time_window)
		

		test = self.dfs[0]


		sensor_col_n = test.shape[1]
		arr_test = np.array([int(self.ends[0]/time_window+1),len(fxn_list*sensor_col_n)])

		for fxn in fxn_list:

			for lb, ub in zip(lower,upper):
				print(lb,ub)

				data = self._slice_df(test,lb,ub)
				
				for i in range(sensor_col_n):

					print(len(data[data.columns[i]]))



				# print(fxn(data))






	def _slice_df(self,df,start,end):
		idx = (df.index>=start) & (df.index<end)
		return df[idx] 














