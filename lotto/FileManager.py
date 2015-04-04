import urllib.request, urllib.parse, urllib.error
import pandas as pd
import time
from datetime import datetime
import os

class LotteryURL():
	def __init__(self, name, url):
		self.name = name
		self.url = url
		self.dirName = self.name.lower() + 'files/'
		self.fileName = self.dirName + self.name + '.txt'


class FileManager(object):
	@classmethod
	def downloadLatestNumbers(self, lotteryURL):
		self.lotteryURL = lotteryURL
		self.dirName = self.lotteryURL.dirName
		self.fileName =  self.lotteryURL.fileName
		

		print('Downloading Latest', self.lotteryURL.name, 'Numbers')
		
		f = urllib.request.urlopen(self.lotteryURL.url)
		data = f.read()

		if not os.path.exists(self.dirName):
			os.makedirs(self.dirName)

		with open(self.fileName, 'wb') as code:
			code.write(data)
		if os.path.isfile(self.fileName):
			print('Download Complete')
		else:
			print('There was an error while downloading the file.')

	@classmethod
	def convertPBToCSV(self, lotteryURL):
		self.lotteryURL = lotteryURL
		file = open(self.lotteryURL.fileName, 'r')
		df = pd.DataFrame(columns =['Date', 'W1', 'W2', 'W3', 'W4', 'W5', 'PB'])
		for line in file:
			if 'Draw Date' not in line:
				data = line.split()
				if len(data) > 7:
					data.pop()

				date_stamp = datetime.strptime(data[0], '%m/%d/%Y').date()
				white_balls = [data[1],data[2],data[3],data[4],data[5]]
				sorted_white_balls = sorted(white_balls)
				power_ball = data[6]

				df = df.append({'Date':date_stamp, 'W1':sorted_white_balls[0],'W2':sorted_white_balls[1],'W3':sorted_white_balls[2],'W4':sorted_white_balls[3],'W5':sorted_white_balls[4],'PB':power_ball}, ignore_index = True)

		save_name_sorted = self.lotteryURL.dirName + self.lotteryURL.name + '_sorted' + '.csv'	

		print('Saving', save_name_sorted.split('/')[1])
		df.to_csv(save_name_sorted)
		print('Complete')

	def updateNumbers():
		url_powerball = LotteryURL('Powerball', 'http://www.powerball.com/powerball/winnums-text.txt')
		FileManager.downloadLatestNumbers(url_powerball)
		FileManager.convertPBToCSV(url_powerball)

		url_superlotto = LotteryURL('SuperLotto', 'http://www.calottery.com/sitecore/content/Miscellaneous/download-numbers/?GameName=superlotto-plus')
		FileManager.downloadLatestNumbers(url_superlotto)

def Main():
	FileManager.updateNumbers()

if __name__ == '__main__':
	Main()