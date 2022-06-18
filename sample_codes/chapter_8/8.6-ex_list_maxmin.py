lst = list()
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        number = float(number)
    except:
        print("Invalid input")
        continue
    lst.append(number)
        
print("Maximum:", max(lst))
print("Minimum:", min(lst))
