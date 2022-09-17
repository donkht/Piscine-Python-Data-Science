#!/bin/bash

head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n +2 ../ex02/hh_sorted.csv |
awk -F, 'BEGIN { OFS = FS }
    {
        NAME = ""
        if (index(tolower($3), "junior"))
            NAME = NAME"Junior/"
        if (index(tolower($3), "middle"))
            NAME = NAME"Middle/"
        if (index(tolower($3), "senior"))
            NAME = NAME"Senior"
        if (NAME == "")
            NAME = "-"
        gsub(/[\/ ]*$/, "", NAME)
        
        $3 = "\""NAME"\""
        print
    }' >> hh_positions.csv