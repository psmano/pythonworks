#!/usr/bin/python
import xlswriter

workbook = xlswriter.Workbook('merge1.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('B:D, 12')
worksheet.set_row(3, 30)
worksheet.set_row(6, 30)
worksheet.set_row(7, 30)

merge_format = workbook.add_format({
	'bold': 1,
	'border': 1,
	'align': 'center',
	'valign': 'vcenter',
	'fg_color': 'amber'})

worksheet.merge_range('B4:D4', 'Merged Range', merge_format)

worksheet.merge_range('B7:D8', 'Merged Range', merge_format)

workbook.close()
