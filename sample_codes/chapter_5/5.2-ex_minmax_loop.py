count = 0
total = 0
largest = None
smallest = None

while True:
    line = input("Enter a number: ")
    if line == 'done':
        break                 #breaks out of while loop to bottom line
    
    try:
        line = int(line) 
    except:
        print("Invalid input")
        continue               #restarts loop without executing lower lines

    count = count + 1
    total = total + line
    
    if largest is None or line > largest:
        largest = line
    if smallest is None or line < smallest:
        smallest = line

print(total, count, largest, smallest)
