#!/bin/bash
#
( ./part01.py 1 1 
./part01.py 3 1
./part01.py 5 1
./part01.py 7 1
./part01.py 1 2
) | awk 'BEGIN {tot = 1} /Tree count/ {print $4; tot = tot * $4} END {print tot}'
