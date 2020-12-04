#!/bin/bash
#
cat input.txt | awk '
BEGIN {
	words = ""
}

{
	if (NF==0) {
		print words
		words = ""
	} else {
		words = words " "  $0
	}
	
}
END {
    print words
}

' | tee tidy.data| awk '
BEGIN {
	good = 0
	n = split("byr iyr eyr hgt hcl ecl pid", codes)
}
{
	invalid = 0
	for (i in codes) {
		n = index($0,codes[i])
		if (n == 0) {
			invalid = 1
		}
	}
	if ( invalid == 0 ) {
		good = good + 1
	}
}
END {
	print good,"valid codes"
}
'
