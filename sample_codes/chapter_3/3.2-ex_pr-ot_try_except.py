# OT Rate total = 1.5 * Rate
# Ideal for bash terminal; in IDLE, put except at end and add the extra ->tabs needed

try:
    hours = input("Enter Hours: ")
    hours = float(hours)
    
    rate = input("Enter Rate: ")
    rate= float(rate)

except:
    print("Error, please enter numeric input")
    quit()

if hours <= 40 :
    pay = hours * rate
    print("Pay:", pay)
        
else :
    ot = hours - 40
    ot = float(ot)
    ot_rate = 0.5 * rate    #1 of 1.5 already included in hours (all of them) * rate
    
    pay = (hours * rate) + (ot_rate * ot)
    print("Pay:", pay)

