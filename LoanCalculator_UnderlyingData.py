# import modules2
import locale
import csv
import calendar
import datetime
locale.setlocale(locale.LC_ALL, 'en_US')

# inputs
startingbalance = float(input('Current Balance: '))
interestrate = float(input('Interest Rate: '))
payment = float(input('Payment: '))
csvname = str(input('Desired Filename: '))

# set dates
today = datetime.date.today()
daysinmonth = calendar.monthrange(today.year, today.month)[1]
dateadd = 0
payperiod = today.strftime('%B %Y')

# prep for csv
c = csv.writer(open(csvname+'.csv', 'w'), lineterminator='\n')
c.writerow(['Period', 'Starting Principal Balance', 'Payment', 'Interest','Principal Payment','Ending Principal Balance'])

# calculations
interest = round(startingbalance * interestrate * daysinmonth / 365, 2)
principalpayment = payment - interest
endingbalance = startingbalance - principalpayment


while endingbalance >= 0:
    #Write to CSV
    c.writerow([payperiod,locale.currency(startingbalance), locale.currency(payment), locale.currency(interest), locale.currency(principalpayment), locale.currency(endingbalance)])

    #Set Dates
    dateadd += 1
    payperiodcalc = today + datetime.timedelta((dateadd+1) * 365 / 12)
    payperiod = payperiodcalc.strftime('%B %Y')
    daysinmonth = calendar.monthrange(payperiodcalc.year, payperiodcalc.month)[1]

    #Financial Calcs
    interest = round(endingbalance * interestrate * daysinmonth / 365, 2)
    principalpayment = payment - interest

    if endingbalance == 0:
        break
    elif endingbalance < principalpayment:
        principalpayment = endingbalance
        endingbalance = endingbalance - endingbalance
        startingbalance = endingbalance + endingbalance
    else: endingbalance = endingbalance - principalpayment
    startingbalance = endingbalance + principalpayment
