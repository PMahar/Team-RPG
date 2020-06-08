import array
import csv
#from tkinter import filedialog
from sys import exit

def parse():

	button = '<button style="left: 5em; top: 5em" class="button" onclick="window.location=\'<!--BUTTON GOTO-->\'"><!--BUTTON LABEL--></button>'

	workingSheet = "sub.csv" #filedialog.askopenfilename(title = 'Open sheet', filetypes = (('CSV Sheets','*.csv'),('All files','*.*')))
	#readSheet = open(workingSheet, 'r')
	print('READ SHEET:' + workingSheet)
	#for x in readSheet:
	#print(x)
	subConf = input('Substitute with this sheet? (Y/N)')
	if subConf == 'y' or subConf == 'Y':
		workingHTML = "game.html" #filedialog.askopenfilename(title = 'Open HTML', filetypes = (('HTML Documents','*.html'),('All files','*.*')))
		rowCount = 0

		with open(workingSheet) as csv_sheet:
			read_csv = csv.reader(csv_sheet, delimiter=',')

			for y in read_csv:
				if rowCount != 0:
					fileGen = open(y[0] + ".html", 'w')
					for x in open(workingHTML, 'r'):
						if '<!--IMAGE GOES HERE-->' in x:
							x = x.replace('<!--IMAGE GOES HERE-->', y[2])
						# more substitutions here...

						# pretend button
						if '<!--BUTTONS HERE-->' in x:
							# But wait....

							# Check to see if y[3] has anything in it to start with, or if it exists at all!
							# if not (eg len(y) < 4), do nothing

							# But there's still more.... We have *at least* 1 button now
							# What is the length of the array y? Ex: 7 items.
							# ex - cont'd: 7 items less 3 static columns == 4
							# number of buttons is 4/2 == 2 buttons
							# Pattern: Button 0 y[3], y[4]
							#                 1 y[5], y[6]
							#                 2 y[7], y[8]
							# so n=3, n+=2 each loop, while n < array length
       
                            				#Start with y[3] for the ID and y[4] for the label, increment both by 2
							i = 3
							l = 4
                      
                           				#Start

							x = x.replace('<!--BUTTONS HERE-->', button)
							x = x.replace('<!--BUTTON GOTO-->', y[i])
							x = x.replace('<!--BUTTON LABEL-->', y[l])
							# ... label is y[4]

							# as you loop, keep working in this 'x'. Each subsequent loop, APPEND the variable button and
							# resubstitute.
							i += 2
							l += 2

						fileGen.write(x)
				rowCount += 1
	else:
		exit(0)

parse()
