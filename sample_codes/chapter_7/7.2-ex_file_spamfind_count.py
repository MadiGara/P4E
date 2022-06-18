fname = input('Enter the file name: ')
count = 0
total = 0
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fh:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        number = line[20:]        #end of number marks end of line
        number = float(number)
        total = total + number
    else:
        continue
avg = total / count
avg = round(avg, 12)        #rounds to 12 digits
print('Average spam confidence:', avg)
