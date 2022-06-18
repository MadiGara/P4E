fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File not accessible", fname)
    exit()
wordic = dict()

for line in fhand:
    line = line.rstrip()
    sline = line.split()
    if not line.startswith("From "): continue
    email = sline[1]
    parts = email.split("@")
    domain = parts[1]
    wordic[domain] = wordic.get(domain,0) + 1
    #adds a count to the address key each loop
print(wordic)
