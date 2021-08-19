#Get the Current Working Folder
import os
os.getcwd()

#Importing openpyxl library
import openpyxl

#Loading the Workbook and printing the object
wb = openpyxl.load_workbook('testExcel.xlsx')
print('Openpyxl Class: ',type(wb))

#Sheets in Excel Workbook
print('Sheets in the Excel file: ',wb.sheetnames)

#Active Sheet in the Workbook
print('Active Worksheet: ',wb.active)

actvSheet = wb.active

#Printing the Column Headers
print("Printing ",actvSheet," contents: ",actvSheet['A1'].value)
print("Printing ",actvSheet," contents: ",actvSheet['B1'].value)
print("Printing ",actvSheet," contents: ",actvSheet['C1'].value)

#Printing the Column Values
print("Printing ",actvSheet," contents: ",actvSheet['A2'].value)
print("Printing ",actvSheet," contents: ",actvSheet['A3'].value)
print("Printing ",actvSheet," contents: ",actvSheet['A4'].value)
print("Printing ",actvSheet," contents: ",actvSheet['A5'].value)
print("Printing ",actvSheet," contents: ",actvSheet['B2'].value)
print("Printing ",actvSheet," contents: ",actvSheet['B3'].value)
print("Printing ",actvSheet," contents: ",actvSheet['B4'].value)
print("Printing ",actvSheet," contents: ",actvSheet['B5'].value)
print("Printing ",actvSheet," contents: ",actvSheet['C2'].value)
print("Printing ",actvSheet," contents: ",actvSheet['C3'].value)
print("Printing ",actvSheet," contents: ",actvSheet['C4'].value)
print("Printing ",actvSheet," contents: ",actvSheet['C5'].value)
