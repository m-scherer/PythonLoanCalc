import csv
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

with open('test.csv', 'r') as file:
    reader = csv.reader(file, delimiter= ',', quotechar='|')
    interestlist = []
    lastline = next(reader)
    for row in reader:
        lastline = row
        interestlist.append(locale.atof(row[3].strip('$')))
    print('Final Payment Date: ',lastline[0])
totalinterest = sum(interestlist)

print('Total Interest Paid: ',locale.currency(totalinterest))


