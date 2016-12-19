#! /usr/bin/python

import os
import sys
import numpy
import math
import getopt

def usage():
	print """
Calcu_Identity.py: reads a .delta.filter.coords output and calculate the percentage of identity among the matches.

Usage: CompEValues.py [-h] <.delta.filter.coords>

-h                  print this help message

<.delta.filter.coords>   the output file of the Mummerplot "show-coords" function. 
"""

o, a = getopt.getopt(sys.argv[1:],'-output:h')
opts = {}

for k,v in o:
	opts[k]=v
if '-h' in opts.keys():
	usage(); sys.exit()

TotalLen=0
IdentLen=0

Coord= sys.argv[1];

try:
	t=open(Coord)
except IOError:
	print("File %s does not exit!!!" % Coord)

filecontent=open(Coord)

for line in filecontent:
	matchlen= line.split()[4]
	ident= line.split()[6]
	TotalLen=TotalLen+int(matchlen)
	IdentLen=IdentLen+int(matchlen)*float(ident)/100

X=IdentLen/TotalLen
print TotalLen;
print IdentLen;
print X;
