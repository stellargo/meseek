#!/usr/bin/python

import sys
import subprocess
from fetcher import fetcher
from openurl import openurl

class bcolors:
	YELLOW = '\033[93m'
	RED = '\033[91m'
	ENDC = '\033[0m'

def main():
	print(bcolors.RED + "Running Meseek v1.0.0" + bcolors.ENDC)

	fixlist = fetcher(sys.argv[1])
	decision = 1
	fix_counter = 1
	
	while (decision!=0):
		
		print("Please select an option:")
		print("1. Open Fix (" + str(fix_counter) + '/' + str(len(fixlist)) + ')')
		print("2. Share Fix with Meseek")
		print("0. Exit")
		decision = int(input())
		
		if (decision==1):
			url = fixlist[fix_counter-1]
			openurl(url)
			fix_counter += 1
			if (fix_counter==len(fixlist)+1):
				print("Meseek is out of solutions :(")
				decision = 0
		
		elif (decision==2):
			#Write code here
			decision=0



if __name__ == '__main__':
	main()