# OT Rate total = 1.5 * Rate
# 0.5 * rate below is because 1.0 of 1.5 is already included in hours * rate

try:
    hours = input("Enter Hours: ")
    hours = float(hours)
    
    rate = input("Enter Rate: ")
    rate= float(rate)

except:
    print("Error, please enter numeric input")
    quit()

def computepay(hours, rate) :
    if hours <= 40 :
        pay = hours * rate
        
    else :
        pay = (hours * rate) + ((0.5 * rate) * (hours-40))

    return(pay)

total_pay = computepay(hours, rate)
print("Pay:", total_pay)

#after running this program (def is established), can do things like
# >>> computepay(45, 10) and have it properly spit out 475.0!
