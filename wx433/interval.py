import re

class Interval():

	def __init__(self, interval=None):
		
		if interval is None:

			self.lower = None
			self.upper = None
			self.lowerBound = ''
			self.upperBound = ''


		else:

			interval = interval.strip()

			if 	interval[0] not in ['[', '(', ')', ']'] or interval[-1] not in ['[', '(', ')', ']']:
				print("Invalid interval")
				raise ValueError

			else:

				try:
					input1 = interval[1:-1]
					numberlist = re.split(", |,", input1)

					self.lower = int(numberlist[0])
					self.upper = int(numberlist[-1])

					self.lowerBound = interval[0]
					self.upperBound = interval[-1]

				except:
					print("Invalid interval")


				if self.lowerBound == "(":
					self.actuallower = self.lower + 1
				else:
					self.actuallower = self.lower

				if self.upperBound == ")":
					self.actualupper = self.upper - 1
				else:
					self.actualupper = self.upper

				if self.actualupper < self.actuallower:
					print("Invalid interval")
					raise ValueError


	def __str__(self):
			return  "{0}{1}, {2}{3}".format(self.lowerBound, self.lower, self.upper, self.upperBound)

	def __repr__(self):
			return  "{0}{1}, {2}{3}".format(self.lowerBound, self.lower, self.upper, self.upperBound)



		
	@staticmethod
	def mergeIntervals(interval1, interval2):
		interval1 = Interval(interval1)
		interval2 = Interval(interval2)

		defualtInterval = Interval() 
		if interval1.actuallower - interval2.actualupper > 1 or interval2.actuallower - interval1.actualupper > 1:		
			return [interval1, interval2]
		
		else:
			if interval1.actuallower == interval2.actualupper or interval1.actuallower - interval2.actualupper == 1:
				defualtInterval.lowerBound = interval2.lowerBound
				defualtInterval.lower = interval2.lower
				defualtInterval.upper = interval1.upper
				defualtInterval.upperBound = interval1.upperBound
				return defualtInterval
			
			elif interval2.actuallower == interval1.actualupper or interval2.actuallower - interval1.actualupper == 1:
				defualtInterval.lowerBound = interval1.lowerBound
				defualtInterval.lower = interval1.lower
				defualtInterval.upper = interval2.upper
				defualtInterval.upperBound = interval2.upperBound
				return defualtInterval
			
			elif interval2.actuallower >= interval1.actuallower:
				#c>=a
				if interval2.lower >= interval1.lower:
					#[c
					defualtInterval.lower = interval1.lower
					defualtInterval.lowerBound = interval1.lowerBound
				else:
					#(c
					defualtInterval.lower = interval2.lower
					defualtInterval.lowerBound = interval2.lowerBound

				if interval2.actualupper >= interval1.actualupper:
					#d>=b
					if interval2.upper >= interval1.upper:
						#d)
						defualtInterval.upper = interval2.upper
						defualtInterval.upperBound = interval2.upperBound
					
					else:
						#d]
						defualtInterval.upper = interval1.upper
						defualtInterval.upperBound = interval1.upperBound
			
				
				else:
					#d<b
					defualtInterval.upper = interval1.upper
					defualtInterval.upperBound = interval1.upperBound
					return defualtInterval
			
			else:
				#c<a
				defualtInterval.lower = interval2.lower
				defualtInterval.lowerBound = interval2.lowerBound
				if interval2.actualupper >= interval1.actualupper:
					#d>b
					if interval2.upper >= interval1.upper:
						#d)
						defualtInterval.upper = interval2.upper
						defualtInterval.upperBound = interval2.upperBound
						return defualtInterval
					else:
						#d]
						defualtInterval.upper = interval1.upper
						defualtInterval.upperBound = interval1.upperBound
				else:
					#d,b
					defualtInterval.upper = interval1.upper
					defualtInterval.upperBound = interval1.upperBound
			return defualtInterval


	@staticmethod
	def mergeOverlapping(intervals):
		intervals = intervals.strip()
		splitList = re.split(", |,", intervals)
		intervals = []
		for i in range(int(len(splitList)/2)):
			origInt = splitList[2*i]+", "+splitList[2*i+1]
			finInt = Interval(origInt)
			intervals.append(finInt)

		
		intervals.sort(key=lambda interval: interval.actuallower)

		newList = []
		newInt = intervals[0]
		for i in range(len(intervals)-1):
			if newInt.actualupper < intervals[i+1].actuallower -1:
				newList.append(newInt)
				newInt = intervals[i+1]
			else:
				if newInt.actualupper >= intervals[i+1].actualupper:
					pass
				else:
					newInt.actualupper = intervals[i+1].actualupper
					newInt.upper = intervals[i+1].upper
					newInt.upperBound = intervals[i+1].upperBound

		newList.append(newInt)

		return newList


	@staticmethod
	def insert(intervals, newint):
		try:
			intervals = intervals + ", " + newint
		except:
			print("Invalid input")
		ans = Interval.mergeOverlapping(intervals)
		return ans
		# except AttributeError:
		# 	print("Invalid input")
		

		# intervals = intervals + ", " + newint
		# splitList = re.split(", |,", intervals)
		# intervals = []
		# for i in range(int(len(splitList)/2)):
		# 	origInt = splitList[2*i]+", "+splitList[2*i+1]
		# 	finInt = Interval(origInt)
		# 	intervals.append(finInt)

		
		# intervals.sort(key=lambda interval: interval.actuallower)

		# newList = []
		# newInt = intervals[0]
		# for i in range(len(intervals)-1):
		# 	if newInt.actualupper < intervals[i+1].actuallower -1:
		# 		newList.append(newInt)
		# 		newInt = intervals[i+1]
		# 	else:
		# 		if newInt.actualupper >= intervals[i+1].actualupper:
		# 			pass
		# 		else:
		# 			newInt.actualupper = intervals[i+1].actualupper
		# 			newInt.upper = intervals[i+1].upper
		# 			newInt.upperBound = intervals[i+1].upperBound

		# newList.append(newInt)

		# return newList



		# # intervals = intervals + ", " + newint
		# # ans = Interval.mergeOverlapping(intervals)
		



# a = Interval.insert("[2, 4), (6, 16)", "[4,6)")



# a = Interval("[2, 4)")
# print(a)
# b = interval("[4,6)")
# c = interval("(-3,5)")
# d = interval("[5, 9]")
# e = interval("(6, 16)")

# print(a)
# print(b)
# print(c)
# print(d)
# # print(e)


# merge_1 = Interval.mergeIntervals("[4,6)", "(-3,5)")
# print(merge_1)
# # merge_2 = interval.mergeIntervals("[4,7)", "[5, 9]")
# # merge_3 = interval.mergeIntervals("[5, 9]", "(6, 16)")
# # # merge_4 = interval.mergeIntervals("(-3,5)", "(6, 16)")
# # # # merge_5 = interval.mergeIntervals(c, b)
# # # # merge_6 = interval.mergeIntervals(d, b)
# # # # merge_7 = interval.mergeIntervals(e, b)
# # # # merge_8 = interval.mergeIntervals(c, e)
# # # # # merge_9 = interval.mergeIntervals(c, d)

# # a = "[2, 4), [4,6), (-3,0), [5, 9], (6, 16)"
# # y = '(-3, 0), [2, 16)'
# b = Interval.mergeOverlapping("[2, 4), [4,6), (-3,0), [5, 9], (6, 16), [24, 32], [101, 250)")
# print(b)
# print(type(b))
# # # # print(type(b[0]))
# # # # print(type(b))


# # # # print(b.extend([a]))

# # a = "(-3, 0), [2, 16)"
# # d = "[-1, 1)"
# # # e = interval(d)
# # # print(e)
# # # print(type(e))

# # # f = b.extend(e)

# # # print(f)
# # # print(type(f))
# # # print(d)
# # # print(type(d))
# c = Interval.insert("[2, 4), [4,6), (-3,0), [5, 9], (6, 16), [24, 32], [101, 250)", "[-36, -24)")
# print(c)

# # print(1, merge_1)
# # print(2, merge_2)
# # print(3, merge_3)
# # print(4, merge_4)
# # print(5, merge_5)
# print(6, merge_6)
# print(7, merge_7)
# print(8, merge_8)



# if __name__ == '__main__':
#     pass