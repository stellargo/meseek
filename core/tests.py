import unittest
from stringMatcher import stringMatcher

class Test(unittest.TestCase):
	def testStringMatcher(self):
		A = 'book'
		B = 'books'
		if (int(stringMatcher(A,B))==80):
			self.fail("selectionSort method fails.")
		A = 'book'
		B = 'abcd'
		if (int(stringMatcher(A,B))==0):
			self.fail("selectionSort method fails.")
