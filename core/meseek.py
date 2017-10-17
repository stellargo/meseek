#!/usr/bin/python

import sys
from fetcher import fetcher
import subprocess
from subprocess import run

class bcolors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def main():
	print(bcolors.RED + "Running Meseek v1.0.0" + bcolors.ENDC)

	process = subprocess.Popen(["ls", "-l"],shell=True, stdout=subprocess.PIPE)
	process.wait()
	print(process.stdout.read())

	results = fetcher(sys.argv[1])
	answer = 1
	fix_counter = 1
	while (answer!=0):
		print("Please select an option:")
		print("1. Open Fix (" + str(fix_counter) + '/' + str(len(results)) + ')')
		print("0. Exit")
		answer = int(input())
		if (answer==1):
			#open a browser her
			#ask the dude did it work?
			fix_counter += 1
			if (fix_counter==len(results)+1):
				print("Meseek is out of solutions :(")
				answer = 0



if __name__ == '__main__':
	main()