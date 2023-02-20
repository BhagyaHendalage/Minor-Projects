#!/bin/bash

files=$(ls *.fasta)
for file in $files
	do
		seq=$(grep -r -l "WGKWVAEIR" $file)
		echo "$seq" >> AP2_basic_headers.txt
	done

