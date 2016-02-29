#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import csv
from sklearn import linear_model
from datetime import datetime

def week(x):
    	return {
        	'Lundi': 1,
        	'Mardi': 2,
		'Mercredi': 3,
		'Jeudi': 4,
		'Vendredi': 5,
		'Samedi': 6,
		'Dimanche': 7
    	}[x]

def day_night(x):
	return{
		'Nuit': 1,
		'Jours': 2
	}[x]

def assignment(x):
	return{
		'CAT': 0,
		'CMS': 1,
		'Crises': 2,
		'Domicile': 3,
		'Gestion': 4,
		'Gestion - Accueil Telephonique': 5,
		'Gestion Amex': 6,
		'Gestion Assurances': 7,
		'Gestion Clients': 8,
		'Gestion DZ': 9,
		'Gestion Relation Clienteles': 10,
		'Gestion Renault': 11,
		'Japon': 12,
		'Manager': 13,
		'Mécanicien': 14,
		'Médical': 15,
		'Nuit': 16,
		'Prestataires': 17,
		'RENAULT': 18,
		'RTC': 19,
		'Regulation Medicale': 20,
		'SAP': 21,
		'Services': 22,
		'Tech. Axa': 23,
		'Tech. Inter': 24,
		'Tech. Total': 25,
		'Téléphonie': 26,
	}.get(x, 27)

dimension = 7
predict = 28
#input_data = pd.read_csv("train_2011_2012.csv",header = 0, sep = ";", encoding = 'utf-8')
#print "Size of the dataset: ", input_data.shape
#rows = (input_data.shape)[0]

initial_time = datetime(2011,1,1,0,0)
last_time = datetime(2013,1,1,0,0)
sizes =int((last_time - initial_time).total_seconds()/1800)
train_data = np.zeros((sizes,dimension))
label = np.zeros((sizes,28))

count = 0
number = 0
with open("train_2011_2012.csv", 'rb') as csvfile:
	reader =csv.DictReader(csvfile,delimiter=';')
	for row in reader:
		tmp_list = row['DATE'].split(' ')
		data_list = tmp_list[0].split('-')
		time_list = tmp_list[1].split(':')
		current_time = datetime(int(data_list[0]),int(data_list[1]),int(data_list[2]),int(time_list[0]),int(time_list[1]))
		t = int((current_time - initial_time).total_seconds()/1800)
		train_data[t][0] = int(row['DAY_OFF'])+1
		if (row['DAY_DS'] == ""):
			train_data[t][1] = 1
		else:
			train_data[t][1] = 2
		train_data[t][2] = int(row['WEEK_END'])
		train_data[t][3] = week(row['DAY_WE_DS'])
		train_data[t][4] = day_night(row['TPER_TEAM'])
		train_data[t][5] = int(row['TPER_HOUR'])
		train_data[t][6] = t
		label[t][int(assignment(row['ASS_ASSIGNMENT']))] += int(row['CSPL_RECEIVED_CALLS'])
		count += 1
		if (count > 10000):
			print number+count
			number += count
			count = 0
#for i in range(rows):
#	tmp_list = input_data.loc[i,'DATE'].split(' ')
#	data_list = tmp_list[0].split('-')
#	time_list = tmp_list[1].split(':')
#	current_time = datetime(int(data_list[0]),int(data_list[1]),int(data_list[2]),int(time_list[0]),int(time_list[1]))
#	t = int((current_time - initial_time).total_seconds()/1800)
#	train_data[t][0] = int(input_data.loc[i,'DAY_OFF'])+1
#	if (input_data.loc[i,'DAY_DS'] == ""):
#		train_data[t][1] = 1
#	else:
#		train_data[t][1] = 2
#	train_data[t][2] = int(input_data.loc[i,'WEEK_END'])
#	train_data[t][3] = week(input_data.loc[i,'DAY_WE_DS'])
#	train_data[t][4] = day_night(input_data.loc[i,'TPER_TEAM'])
#	train_data[t][5] = int(input_data.loc[i,'TPER_HOUR'])
#	train_data[t][6] = t
#	label[t][int(assignment(input_data.loc[i,'ASS_ASSIGNMENT']))] += 1

f = open("filter.txt",'w')
for i in range(sizes):
	if (train_data[i][6] == 0):
		continue;
	for j in range(dimension):
		f.write(str(int(train_data[i][j]))+" ")
	for j in range(predict):
		f.write(str(int(label[i][j]))+" ")
	f.write("\n")
	
	
	
