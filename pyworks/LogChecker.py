#!usr/bin/env python

logfile = open("C://Manohar//Python//PythonBasics//testLog.log","r")
for line in logfile:
    line_split = line.split()
    print(line_split)
    listy = line_split[0], line_split[1], line_split[2], line_split[4]
    print(listy)
