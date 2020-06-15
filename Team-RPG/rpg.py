import array
import csv
# from tkinter import filedialog
from sys import exit


def parse():
    button = '<button style="left: <!--L JUST-->; top: <!--T JUST-->" class="button" onclick="window.location=\'<!--BUTTON GOTO-->\'"><!--BUTTON LABEL--></button>'

    workingSheet = "sub.csv"
    print('READ SHEET:' + workingSheet)
    subConf = input('Substitute with this sheet? (Y/N)')
    if subConf == 'y' or subConf == 'Y':
        workingHTML = "game.html"
        rowCount = 0

        with open(workingSheet) as csv_sheet:
            read_csv = csv.reader(csv_sheet, delimiter=',')
            for y in read_csv:
                horizJ = 2
                vertJ = 1
                if rowCount != 0:
                    fileGen = open(y[0] + ".html", 'w')
                    for x in open(workingHTML, 'r'):
                        # Begin counters for button goto, label, and position later on
                        i = 3
                        l = 4
                        if '<!--IMAGE HERE-->' in x:
                            x = x.replace('<!--IMAGE HERE-->', y[2])

                        if '<!--PROMPT HERE-->' in x:
                            x = x.replace('<!--PROMPT HERE-->', y[1])

                        if '<!--PROMPT SIZE HERE-->' in x:
                            if 0 < len(y[1]) < 150:
                                subSize = "40"
                            elif 150 < len(y[1]) < 250:
                                subSize = "30"
                            elif 250 < len(y[1]) < 350:
                                subSize = "25"
                            x = x.replace('<!--PROMPT SIZE HERE-->', subSize + 'px')

                        if '<!--BUTTONS HERE-->' in x:
                            while l < len(y) and len(y[i]) > 0 and len(y[l]) > 0:
                                if i > 3:
                                    x += "\n" + "	" + button
                                else:
                                    x = x.replace('<!--BUTTONS HERE-->', '	' + button)

                                x = x.replace('<!--BUTTON GOTO-->', y[i] + '.html')
                                x = x.replace('<!--BUTTON LABEL-->', y[l])

                                #If the remainder of the positional counters divided by 2 is zero (i.e., they're
                                #even), use them for positioning. The counters inversely oscillate

                                #Because we're generating buttons by rows, add to the vertical justify only when
                                #we're done with one horizontal row at a time (So only increment horizontally
                                #when vertJ isn't even)

                                #if horizJ % 2 != 0:
                                #    lJust = '1em'
                                #    horizJ += 1
                                #else:
                                #    lJust = '5em'
                                #    horizJ += 1

                                #Or, ya know, screw it because automatically centering buttons is difficult
                                vertJ += 4

                                #x = x.replace('<!--L JUST-->', lJust)
                                x = x.replace('<!--T JUST-->', str(vertJ) + 'em')

                                i += 2
                                l += 2

                        fileGen.write(x)
                rowCount += 1
    else:
        exit(0)


parse()
