""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

# Build your code below

bill = input('How much is your total bill?')
payment = input('How much is your payment?')

if float(payment) < float(bill):
    print ('Sorry, but your payment is not enough for your bill')
elif float(payment) >= float(bill):
    total = (float(payment) - float(bill))
    roundTotal = round(total, 2)
    if float(roundTotal) == 0.0:
        print('Hi! Thank you for your payment! Please come again.')
    elif float(roundTotal) > 0.0:
        print('Hi! Your change is ' + str(roundTotal) )

