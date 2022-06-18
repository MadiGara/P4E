print('python shout.py')
fname = input('Enter a file name: ')
try:
    fh = open(fname)
    #does not like it if file opening is in different folder than code
    #would have to go through bash to open to give permissions (pwd)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fh:
    lines = line.rstrip()
    print(lines.upper())
