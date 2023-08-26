import matplotlib as plt
import numpy as np
import csv


plt.use('Qt5Agg')


with open('QQQ.csv', newline='') as file:
	spamreader = csv.DictReader(file, delimiter=',')
	for row in spamreader:
		print(row['Date'], '|', row['Close'])


print(plt.get_backend())
