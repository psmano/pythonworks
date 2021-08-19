import xlrd
import os

workbook3 = xlrd.open_workbook('Report3.xls', logfile=open(os.devnull, 'w'))
worksheet3 = workbook3.sheet_by_index(0)
num_cols3 = worksheet3.ncols
num_rows3 = worksheet3.nrows
for row_index3 in range(0, num_rows3):
    for col_index3 in range(0, num_cols3):
        cell_val= worksheet3.cell(row_index3, col_index3).value
        with open("outputfile.txt", 'a') as f:
            f.write(str(cell_val))
print ("Write Completed")