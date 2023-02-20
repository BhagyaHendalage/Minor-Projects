#!/bin/bash
files=$(ls *.fasta)
  for i in $files
    do
      pat=$(grep -E -r -l "WGKWV|AAEIR" $i)
      echo "$pat" >> des_contain.txt
    done
header=$(grep -e ">" des_contain.txt)
echo "$header" >> AP2_advanced_headers.txt
