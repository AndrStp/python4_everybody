#Solution for Exercise 6 in Chapter 4 of
#

hours=input('Enter hours: ')
rate=input('Enter rate: ')

try:
    hours=float(hours)
    rate=float(rate)
except:
    print('Bad!!!')
    quit()

def computepay (hours, rate):
    if hours>40:
        norm_hours=40
        norm_pay=norm_hours*rate
        over_pay=(hours-norm_hours)*(rate*1.5)
        final_pay=norm_pay+over_pay
        print('Overpay: ', final_pay)
        
    else:
        norm_pay=hours*rate
        print('Normal pay: ', norm_pay)
        
computepay(float(hours), float(rate))
