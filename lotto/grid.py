import numpy as np
from pandas import *

import pandas as pd
import random



class Position:

	def __init__(self, x, y): # X is the Column Y is the Row
		self.x = x
		self.y = y
		self.pos = (x, y)

class Matrix(Position):

	ROWLETTERS = 'A B C D E F G H I J'

	ROWS = len(ROWLETTERS.split())

	COLUMNS = 6



	def __init__(self):
		self.grid = self.create_grid()

	def create_grid(self):
		self.df = []
		for x in range(self.ROWS):
			self.df.append({'1':'00', '2':'00', '3':'00', '4':'00', '5':'00', '6':'00'})
		self.df = pd.DataFrame(self.df)
		self.df.index = self.ROWLETTERS.split()
		return self.df

	def display(self):
		print(self.grid)

	def get_item(self, x, y):
		return self.grid[x][y]

	def chg_item(self, x, y, value):
		self.grid[x][y] = '%02d' % value

	def chg_row(self, y, values):
		for idx,x in enumerate(range(self.COLUMNS)):
			self.chg_item(str(x+1), y, values[idx])
	
	def mk_random_row(self, y):
		self.chg_row(y, self.mk_random_numbers())

	def mk_random_grid(self):
		for row in self.ROWLETTERS.split():
			self.mk_random_row(row)

	def mk_random_numbers(self): # makes a list of 5 random numbers between 1 - 59 and a Powernumber between 1 - 35
		self.lottoNumbers = []
		self.WB = list(range(1, 60))
		for i in range(5):
			self.value = random.choice(self.WB)
			self.WB.remove(self.value)
			self.lottoNumbers.append(self.value)
		self.lottoNumbers = sorted(self.lottoNumbers)
		self.lottoNumbers.append(random.randint(1, 36))
		return self.lottoNumbers

	def shf_item(self, x, y, xx, yy):
		value_to_shf = self.get_item(x, y)
		self.chg_item(xx, yy, int(value_to_shf))


def Main():

	game_matrix = Matrix()
	game_matrix.display()
	game_matrix.chg_item(x='2', y='A', value=7)
	print(game_matrix.get_item(x='2', y='A'))
	game_matrix.display()
	print(game_matrix.mk_random_numbers())
	game_matrix.mk_random_row('A')
	game_matrix.display()
	game_matrix.mk_random_grid()
	
	# game_matrix.grid['1'].apply(int).hist()
	# print(game_matrix.grid.applymap(int))
	# game_matrix.grid.plot(kind='kde', figsize=(15,10))
	game_matrix.shf_item('2','A','2','B')
	game_matrix.display()


if __name__ == "__main__":
	Main()
