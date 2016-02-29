#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import csv
from sklearn import linear_model
from datetime import datetime

count = 0
f = open("first10000.csv","w")
with open("train_2011_2012.csv", 'rb') as csvfile:
	reader = csv.reader(csvfile,delimiter=';')
	for row in reader:
		lists = [unicode(cell,'utf-8') for cell in row]
		for cell in lists:
			f.write(cell.encode('utf-8') + ';')
		f.write('\n')
		count += 1
		if (count == 10000):
			break;
	
