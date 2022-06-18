print("python fromcount.py")
fname = input("Enter a file name: ")
fhand = open(fname)
count = 0

for line in fhand:
    if not line.startswith("From "): continue
    count = count + 1
    words = line.split()
    print(words[1])
print("There were", count, "lines in the file with From as the first word")
