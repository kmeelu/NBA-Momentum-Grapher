import csv as csv
import numpy as np
import os
import sys
import re
import matplotlib.pyplot as plt

total_games_2011 = 35525

def find_time (time):
	num = (47 - float(time[2:4])) + (60 - float(time[5:7]))/60
	return round(num, 3)

def calc_momentum(data, row):
	team_A = row[0][8:11]
	team_B = row[0][11:14]
	times = []
	points_a = []
	points_b = []
	i = 0
	while (data[i, 0] != row[0]):
		i += 1
		if (i == total_games_2011):
			print "\tGame not found"
			return

	while (data[i,0] == row[0]):
		scored = re.match(r'\[([A-Z]{3}) ([0-9]+)[-]{1}([0-9]+)\]', data[i,3])
		if scored:
			times.append(find_time(data[i,2]))
			if (scored.group(1) == team_A):
			 	points_a.append(int(scored.group(2)))
			 	points_b.append(int(scored.group(3)))
			if (scored.group(1) == team_B):
			 	points_a.append(int(scored.group(3)))
			 	points_b.append(int(scored.group(2)))

		i += 1
		if (i == total_games_2011):
			break
	return (times, points_a, points_b)

def main():
	csv_file_object = csv.reader(open('2011_playbplay.csv', 'rU'))
	header = csv_file_object.next()
	data = []
	print header

	for row in csv_file_object:
		data.append(row[0:])
	data = np.array(data)

	game = calc_momentum(data, data[0])
	plt.figure(figsize=(6 * 1.618, 6))
	plt.xlabel('time')
	plt.ylabel('points')
	plt.plot(game[0], game[1], 'bs', game[0], game[2], 'g^')
	plt.show()


if __name__ == '__main__':
	main()