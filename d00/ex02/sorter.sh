#!/bin/sh

f="../ex01/hh.csv"
cat $f | head -n 1 > hh_sorted.csv 
cat $f | tail -n +2 | sort -t "," -k2,2 -k1,1n  >> hh_sorted.csv