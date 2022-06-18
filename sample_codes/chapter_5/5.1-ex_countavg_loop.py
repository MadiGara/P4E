count = 0
total = 0

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

print(total, count, (total/count))
