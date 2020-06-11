import array
import csv
#from tkinter import filedialog
from sys import exit

def parse():

	button = '<button style="left: 5em; top: 5em" class="button" onclick="window.location=\'<!--BUTTON GOTO-->\'"><!--BUTTON LABEL--></button>'

	workingSheet = "sub.csv"
	print('READ SHEET:' + workingSheet)
	subConf = input('Substitute with this sheet? (Y/N)')
	if subConf == 'y' or subConf == 'Y':
		workingHTML = "game.html"
		rowCount = 0

		with open(workingSheet) as csv_sheet:
			read_csv = csv.reader(csv_sheet, delimiter=',')
			for y in read_csv:
				if rowCount != 0:
					fileGen = open(y[0] + ".html", 'w')
					for x in open(workingHTML, 'r'):
						#Begin counters for button goto and label later on
						i = 3
						l = 4
						if '<!--IMAGE HERE-->' in x:
							x = x.replace('<!--IMAGE HERE-->', y[2])

						if '<!--PROMPT HERE-->' in x:
							x = x.replace('<!--PROMPT HERE-->', y[1])

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

						# Start with y[3] for the ID and y[4] for the label, increment both by 2

							#<!--BUTTONS HERE--> is an obvious starting point for buttons, but buttons must be
							#generated after for every column with information
							x = x.replace('<!--BUTTONS HERE-->', '	' + button)
							x = x.replace('<!--BUTTON GOTO-->', y[i] + '.html')
							# ... label is y[4]
							x = x.replace('<!--BUTTON LABEL-->', y[l])
							# as you loop, keep working in this 'x'. Each subsequent loop, APPEND the variable button and
							# resubstitute.
							#If there's anything in the columns past the image ID, they are button IDs and text
							#If len(y) > 4, make a new button
							
							if len(y[l]) > 0:
								print("i:" + str(i))
								print("l:" + str(l))
								print((len(y[i])))
								x += "\n" + "	" + button
								x = x.replace('<!--BUTTON GOTO-->', y[i] + '.html')
								x = x.replace('<!--BUTTON LABEL-->', y[l])
								i += 2
								l += 2
						fileGen.write(x)
				rowCount += 1
	else:
		exit(0)

parse()
