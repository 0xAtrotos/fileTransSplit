import sys
import csv
import time
import pickle
import os

infile = sys.argv[1]

unisfile = open(infile)

csvReader = csv.reader(thefile, delimiter='$')
header = next(csvReader)

policyIndex = header.index("1")
col1 = header.index("1")
col2 = header.index("2")
col3 = header.index("3")
col4 = header.index("4")
col5 = header.index("5")

de = "$"

prevtran = ""

transactList = []

initial = True
counter = 0
counter2 = 0
allcount = 0
current = "initial"
previous = ""
limit = 950

filen = []
filecount = 0

credit = 0.0
debit = 0.0

for row in csvReader:
    current = row[policyIndex]

    #2017 04 30 0212
    filecol = row[col1]
    idcol = filecol[0:8]+str(filecount).zfill(4)

    if (row[col5] == "1"): #let's say that last column defines credit or debit
        credit += float(row[col13])
    else:
        debit = debit - float(row[col13])

    line = idcol + de + row[col2] + de + row[col3] + de + row[col4] + de + row[col5]

    if ((initial == True) or (current == previous) or (current[0:8] == previous[10:18])):
        initial = False
        transactList.append(line)
    else:
        if (counter2 <= 950):
            transactList.append(line)
        else:
            counter2 = 0
            counter = 0
            directory = os.path.expanduser("~\\Desktop\\Export\\"+row[col1]+"\\")
            if not os.path.exists(directory):
                os.makedirs(directory)
            filen.append(os.path.expanduser(directory+idcol+".txt"))
            allcount += 1
            filename = filen[filecount]
            f = open(filename, "w")
            f.write("\n".join(map(lambda x: str(x), transactList)) + "\n")
            f.close()
            filecount += 1
            del transactList[:]
            firstline = filecount
            idcol2 = filecol[0:8]+str(firstline).zfill(4)
            line2 = idcol2 + de + row[col2] + de + row[col3] + de + row[col4] + de + row[col5]
            transactList.append(line2)

    counter += 1
    counter2 += 1
    previous = current

i = 0
print("\n\n\n")
print("\t\t\tCredit: " + "{0:.2f}".format(credit))
print("\t\t\tDebit: " + "{0:.2f}".format(debit))
print("\t\t\tBalance: " + "{0:.2f}".format(debit+credit))
print("\n\n\n")
print("\t", end="", flush=True)
print("\t\t\tNow Exporting")
while (i != 50):
    print('.', end='', flush=True)
    time.sleep(0.2)
    i += 1

directory = os.path.expanduser("~\\Desktop\\Export\\"+row[col1]+"\\")
if not os.path.exists(directory):
    os.makedirs(directory)
filen.append(os.path.expanduser(directory+idcol+".txt"))
allcount += 1
filename = filen[filecount]
f = open(filename, "w")
f.write("\n".join(map(lambda x: str(x), transactList)) + "\n")
f.close()

print("\n\n\tData has been split into multiple files")
print("\n\n")
print("\n\n\t\t\tPress any key to exit")
input()
print("\t\t\tBye bye...")
time.sleep(2)
