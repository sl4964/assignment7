'''
Created on 2016/11/08
Version: 1.0
@author: liusheng
ShengLiu Copyright 2016

'''

from interval import interval
import sys

def main():
	while True:
		try:
			list_of_intervals = input("List of intervals? ")
			if list_of_intervals == 'quit':
				print ('')
				sys.exit(1)

			list_of_intervals = interval.mergeOverlapping(list_of_intervals)
			break
		except KeyboardInterrupt:
			sys.exit(1)
		except Exception:
			print ('Invalid list of intervals')
			pass

	while True:
		try:
			interv = input('Interval? ')
			if interv == 'quit':
				print ('')
				break
			else:
				interval(interv)
				list_of_intervals = interval.insert(list_of_intervals, interv)
				print (list_of_intervals)
		except KeyboardInterrupt:
			sys.exit(1)
		except:
			print ('Invalid interval')

if __name__ == '__main__':
	main()
