#!/usr/bin/python

import sys
import subprocess
import itertools
import threading
import time
from fetcher import fetcher
from openurl import openurl
from querycleaner import querycleaner

class bcolors:
	BLUE = '\033[0;36m'
	ENDC = '\033[0m'

def main():
	print(bcolors.BLUE + "Running Meseek v1.0.0" + bcolors.ENDC)
	query = ''

	if (sys.argv[1] == '--custom' or sys.argv[1] == '-c'):
		i=2
		while (i<len(sys.argv)):
			query = query + sys.argv[i]
			i+=1
	else:
		i=1
		command = []
		while (i<len(sys.argv)):
			# command = sys.argv[i] + ' '
			command.append(sys.argv[i])
			i+=1
		try:
			process = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		except FileNotFoundError:
			query = FileNotFoundError
		
		if (query!=''):
			query = querycleaner(query)
		elif (process.returncode==0):
			query = str(process.stdout)
			query = querycleaner(query)
			print (bcolors.BLUE + "Command executed with no issues." + bcolors.ENDC)
			return
		else:
			query = str(process.stderr)
			query = querycleaner(query)

	fixlist = fetcher (query)

	decision = 1
	fix_counter = 1
	
	while (decision!=0):
		if (len(fixlist)==0):
			print(bcolors.BLUE + "No Fix available" + bcolors.ENDC)
			return
		print("==="+query)
		print(bcolors.BLUE + "Please select an option:")
		print("1. Open Fix (" + str(fix_counter) + '/' + str(len(fixlist)) + ')')
		print("2. Share Fix with Meseek")
		print("0. Exit"  + bcolors.ENDC)
		decision = int(input())
		
		if (decision==1):
			url = fixlist[fix_counter-1]
			openurl(url)
			fix_counter += 1
			if (fix_counter==len(fixlist)+1):
				print(bcolors.BLUE + "Meseek ran out of solutions" + bcolors.ENDC)
				decision = 0
		
		elif (decision==2):
			#Write code here
			decision=0

		else:
			print(bcolors.BLUE + "Not a valid option. Exiting." + bcolors.ENDC)
			decision=0

if __name__ == '__main__':
	main()