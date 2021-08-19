import openpyxl, csv
import os

wb = openpyxl.load_workbook('excel1.xlsx')
#type(wb)

print("Current Working Directory is: " + os.getcwd())
print("The wb type is: " + str(wb))

print('Getting Sheet Names: ' + str(wb.sheetnames))
print(wb.get_active_sheet())


# sheet = wb.get_sheet_by_name('Sheet3')
# print("Get Sheet by name: " + str(sheet.title))

# anotherSheet = wb.active
# print("Printing Another Sheet: " + str(anotherSheet))

