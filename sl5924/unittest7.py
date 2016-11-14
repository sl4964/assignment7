'''
Created on 2016/11/08
Version: 1.0
@author: liusheng
ShengLiu Copyright 2016
'''
import sys
import unittest
from interval import interval



class  utest(unittest.TestCase):
	def setUp(self):
		pass
	def test_interval(self):
		self.assertEqual(interval('[2,6]').interval2str(),'[2,6]')
		self.assertEqual(interval('(2,6]').interval2str(),'(2,6]')
		self.assertEqual(interval('(2,6)').interval2str(),'(2,6)')
		self.assertEqual(interval('[2,6]').interval2str(),'[2,6]')

	def test_merge_interval(self):
		self.assertEqual(interval.mergeIntervals(interval('[2,6]'),interval('[3,8]')).interval2str(),'[2,8]')
		self.assertEqual(interval.mergeIntervals(interval('(0,12]'),interval('[3,13]')).interval2str(),'(0,13]')
		self.assertEqual(interval.mergeIntervals(interval('(0,12]'),interval('[3,4]')).interval2str(),'(0,12]')
		self.assertEqual(interval.mergeIntervals(interval('(0,3]'),interval('(3,4]')).interval2str(),'(0,4]')
		self.assertEqual(interval.mergeIntervals(interval('[1,3]'), interval('[2,5]')).interval2str(), '[1,5]')
		self.assertEqual(interval.mergeIntervals(interval('(1,13)'), interval('[2,25]')).interval2str(), '(1,25]')
	def test_merge_overlappings(self):
		self.assertEqual(interval.mergeOverlapping('[-10,-7], (-8,1], [3,6), (4,12), [15,23]'), '[-10,1], [3,12), [15,23]')
		self.assertEqual(interval.mergeOverlapping('[1,5],[2,6),(8,10],[8,18]'), '[1,5], [8,18]')
	def test_insert(self):
		self.assertEqual(interval.insert('[1,2), [3,6], (6,8]', '[4,7]'),'[1,2), [3,8]')
	def test_is_Adjacent(self):
		self.assertEqual(interval.isAdjacent(interval('[1,3]'), interval('(3,8)')),1)
		self.assertEqual(interval.isAdjacent(interval('[1,3)'), interval('(3,8)')),2)

	def test_is_Overlap(self):
		self.assertEqual(interval.isOverlap(interval('[1,5)'),interval('[3,8]')),1)
		self.assertEqual(interval.insert('[1,3],[6,9]', '[2,5]'), '[1,9]')
		self.assertEqual(interval.insert('[1,2], (3,5), [6,7), (8,10], [12,16]', '[4,9]'), '[1,2], (3,10], [12,16]')


if __name__ == '__main__':
	unittest.main()

