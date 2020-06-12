import array
import csv
# from tkinter import filedialog
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
                        # Begin counters for button goto and label later on
                        i = 3
                        l = 4
                        if '<!--IMAGE HERE-->' in x:
                            x = x.replace('<!--IMAGE HERE-->', y[2])

                        if '<!--PROMPT HERE-->' in x:
                            x = x.replace('<!--PROMPT HERE-->', y[1])

                        if '<!--BUTTONS HERE-->' in x:
                            print(len(y))
                            while l < len(y) and len(y[i]) > 0 and len(y[l]) > 0:
                                if i > 3:
                                    x += "\n" + "	" + button
                                else:
                                    x = x.replace('<!--BUTTONS HERE-->', '	' + button)

                                print("i:" + str(i))
                                print("l:" + str(l))
                                x = x.replace('<!--BUTTON GOTO-->', y[i] + '.html')
                                x = x.replace('<!--BUTTON LABEL-->', y[l])
                                i += 2
                                l += 2

                        fileGen.write(x)
                rowCount += 1
    else:
        exit(0)


parse()