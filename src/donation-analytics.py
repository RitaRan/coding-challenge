#!/usr/bin/env python3
import sys

from Contribution import * 
from Recipient import * 
from Donor import * 


def parse_contrib(path1, path2, path3):
	# get percentile
	percentile = float(open(path2, "r").read().strip())
	# parse each line
	donors = Donors()
	recipients = Recipients(percentile)
	printout = ''
	with open(path1, "r") as inputfile, open(path3,"w") as outfile:
		for line in inputfile:
			contrib = Contribution(line)
			if not contrib.is_valid():
				continue

			is_repeat_donor = donors.add_donor(contrib)
			if not is_repeat_donor:
				continue

			printout = recipients.add_recipient(contrib)
			outfile.write(printout+'\n')

def main(argv):
	contrib_path = argv[1]
	perc_path = argv[2]
	out_path = argv[3]
	print("Output file path: ", out_path)

	parse_contrib(contrib_path, perc_path, out_path)

if __name__ == "__main__":
	main(sys.argv)
