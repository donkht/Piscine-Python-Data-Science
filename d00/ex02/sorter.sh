#!/bin/sh
(cat "../ex01/hh.csv" | head -n 1; 
 cat "../ex01/hh.csv" | tail -n +2 | sort -t "," -k2 -k1n ) > hh_sorted.csv