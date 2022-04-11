# M4V_M4N, 4/1/22, Brutus: Directory bruteforcer (Averaging 0.2 seconds/ request)
# ToFix: find way to get rid of line delimiter from txt, returns the wrong status code
# ToDo: import wordlist as dictinary, for loop to concat dirs to url, return results, time outs (defualt 1)
# add more perams(-o output to file, -q quiet mode, -t timeout, etc.), ssl cert verification
from typing import Counter
import requests, argparse, sys, time
from datetime import datetime, time

# Construct arg objs
parser = argparse.ArgumentParser(description="Directory bruteforcer")
parser.add_argument("-u", "--url", help="url", dest="url")
parser.add_argument("-w", "--wordlist", help="wordlist", dest="wordlist_path")

# (Formally arg_group)
flag_args = parser.add_mutually_exclusive_group()
flag_args = parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true", dest="verbose")

args = parser.parse_args()
url = args.url
wordlist_path = args.wordlist_path
verbose = args.verbose

if args.verbose:
    print("verbosity turned on")

def start_enum(url, wordlist_path):
	startTime = datetime.now()

	# Get status code of dirs
	print("[*] Starting Brutus...", datetime.now())
	
	# Read in the wordlist
	with open(wordlist_path) as f:
		wordlist = [i.rstrip() for i in f]
	
	# Iterate through wordlist
	for directory in wordlist:
		new_url = url + '/' + directory
		if args.verbose == True:
			print("[*]", new_url, '\t', get_response(new_url))
		elif get_response(new_url) != 404 and args.verbose == False:
			print("[*]", new_url, '\t', get_response(new_url))
	stop_enum(startTime)

def stop_enum(startTime):
	stopTime = datetime.now()
	print("[*] Stopping Brutus...", datetime.now(), f"\nEnumeration finished in {stopTime - startTime}")
	# Write found dirs to screen -here-

def get_response(url):
	response = requests.get(url)
	return response.status_code

start_enum(url, wordlist_path)