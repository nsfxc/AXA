import pandas as pd
import numpy as np
from sklearn import linear_model
from datetime import datetime

def week(x):
    	return {
        	'Lundi': 1,
        	'Mardi': 2,
		'Mecredi': 3,
		'Jeudi': 4,
		'Vendredi': 5,
		'Samdi': 6,
		'Dimanche': 7
    	}[x]

def day_night(x):
	return{
		'Nuit':1,
		'Jour':2
	}[x]

rows = 10
dimension = 7
input_data = pd.read_csv("train_2011_2012.csv",header = 0, sep = ";", nrows = rows, encoding = 'utf-8')
print "Size of the dataset: ", input_data.shape

initial_time = datetime(2011,1,1,0,0)
last_time = datetime(2013,1,1,0,0)
sizes =int((last_time - initial_time).total_seconds()/1800)
train_data = np.zeros((sizes,dimension))
label = np.zeros(sizes)

for i in range(rows):
	tmp_list = input_data.loc[i,'DATE'].split(' ')
	data_list = tmp_list[0].split('-')
	time_list = tmp_list[1].split(':')
	current_time = datetime(int(data_list[0]),int(data_list[1]),int(data_list[2]),int(time_list[0]),int(time_list[1]))
	t = (current_time - initial_time).seconds/1800
	train_data[t][0] = int(input_data.loc[i,'DAY_OFF'])+1
	if (input_data.loc[i,'DAY_DS'] == ""):
		train_data[t][1] = 1
	else:
		train_data[t][1] = 2
	train_data[t][2] = int(input_data.loc[i,'WEEK_END'])
	train_data[t][3] = week(input_data.loc[i,'DAY_WE_DS'])
	train_data[t][4] = day_night(input_data.loc[i,'TPER_TEAM'])
	train_data[t][5] = int(input_data.loc[i,'TPER_HOUR'])
	train_data[t][6] = t
	if (input_data.loc[i,'ASS_ASSIGNMENT'] == 'Finances PCX'):
		++label[t]

clf = linear_model.LinearRegression()
clf.fit(train_data, label)
	
	
	
