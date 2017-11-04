import unittest
from stringMatcher import stringMatcher

class Test(unittest.TestCase):
	def testStringMatcher(self):
		A = 'book'
		B = 'books'
		if (stringMatcher(A,B)!=80.0):
			self.fail("stringMatcher method fails.")
		A = 'book'
		B = 'abcd'
		if (stringMatcher(A,B)!=0.0):
			self.fail("stringMatcher method fails.")
