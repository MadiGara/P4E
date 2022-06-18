fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) < 3 or words[0] != 'From': continue
    print(words[2])
    
#len(words) == 0 is encapsulated in len(words) < 3
#words[0] cond must come after len(words) cond or else will cause error
#because or statement will eval != 'From' first and then skip the line, causes
    #issues if from doesn't have 2 words after it because that if statement
    #was skipped once the != From one was found true
