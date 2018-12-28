import random
import time
 
 
class Sudoku(object):
	def __init__(self):
		self.digits = [[] for i in range(9)]
 
	def make_digits(self):
		col_lists = [[] for i in range(9)]
		area_lists = [[] for i in range(3)]
		nine = self.random_nine()
		for i in range(9):
			col_lists[i].append(nine[i])
		area_lists[0] = nine[0:3]
		area_lists[1] = nine[3:6]
		area_lists[2] = nine[6:]
 
		for i in range(8):
			nine = self.random_nine()
			if i % 3 == 2:
				area_lists[0] = []
				area_lists[1] = []
				area_lists[2] = []
			for j in range(9):
				area_index = j // 3
				count = 0
				error = False
				while nine[0] in col_lists[j] or nine[0] in area_lists[area_index]:
					count += 1
					if count >= len(nine):
						error = True
						break
					nine.append(nine.pop(0))
				if error:
					return False
				first = nine.pop(0)
				col_lists[j].append(first)
				area_lists[area_index].append(first)
		self.digits = col_lists
		return True
 
 
	def random_nine(self):
		nine = [i + 1 for i in range(9)]
		for i in range(5):
			nine.append(nine.pop(random.randint(0, 8)))
		return nine
 
 
if __name__ == '__main__':
	sudoku = Sudoku()
	f = open('Digits.txt', 'a+')
	start = time.time()
	for i in range(500):
		loop = 0
		while not sudoku.make_digits():
			loop += 1
			if loop > 100:
				break
		if loop < 100:
			print('No.{0} Sudoku Digits...'.format(i + 1))
			for col in sudoku.digits:
				for digit in col:
					f.write('{0}  '.format(digit))
				f.write('\n')
			f.write('\n\n\n')
	f.close()
	print('{0} seconds used...'.format(int(time.time() - start)))