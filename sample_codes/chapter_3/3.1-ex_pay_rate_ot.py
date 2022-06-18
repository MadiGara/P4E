# Hours = 45
# Rate = 10
# OT Rate total = 1.5 * Rate

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

hours = float(hours)
rate= float(rate)

if hours <= 40 :
    pay = hours * rate
    print("Pay:", pay)

else :
    ot = hours - 40
    ot = float(ot)
    ot_rate = 0.5 * rate    #1 of 1.5 already included in hours (all of them) * rate
    
    pay = (hours * rate) + (ot_rate * ot)
    print("Pay:", pay)
