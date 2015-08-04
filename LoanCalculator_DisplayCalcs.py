import csv
import locale
import LoanCalculator_UnderlyingData as LCU
locale.setlocale(locale.LC_ALL, 'en_US')

with open(LCU.csvname+'.csv', 'r') as file:
    reader = csv.reader(file, delimiter= ',', quotechar='|')
    interestlist = []
    lastline = next(reader)
    for row in reader:
        try:
            lastline = row
            interestlist.append(locale.atof(row[3].strip('$')))
        except StopIteration:
            break
        print('Final Payment Date: ',lastline[0])
totalinterest = sum(interestlist)

print('Total Interest Paid: ',locale.currency(totalinterest))
