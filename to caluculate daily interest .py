amount=float(input('enter the amount taken for interest:'))
interest=float(input('enter the interest of 100 rs per a day ='))
value=amount/100
perday= value*interest
noofdays=int(input('enter the no of days to pay the interest'))
totalamount=amount+(perday*noofdays)
print('total amountwith interest is=')
print(totalamount)
