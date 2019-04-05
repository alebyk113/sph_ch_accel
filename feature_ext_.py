
import json
import os
import numpy as np

class Feature_extraction:
	def __init__(self,data_path, dfs):
		
		self.data_path = data_path
		self.dfs = dfs

		self.file_list = [f for f in os.listdir(self.data_path) if not f.startswith('.')]    

		self.ends=[]

		for fi, file_id in enumerate(self.file_list):
			self.meta = json.load(open(os.path.join(self.data_path,file_id, 'meta.json')))
			self.ends.append(self.meta['end'])
		


	def get_features(self,time_window):
		'''time_window in ms'''

		lower = np.arange(0,self.ends[0],time_window)
		upper = np.arange(time_window,self.ends[0]+time_window,time_window)
		
		test = self.dfs[0]
		print(self.ends[0])

		for lb, ub in zip(lower,upper):
			print(lb,ub)



			print(self._slice_df(test,lb,ub))




	def _slice_df(self,df,start,end):
		
		idx = (df.index>=start) & (df.index<end)
		
		return df[idx] 














