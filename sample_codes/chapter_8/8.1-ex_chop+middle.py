def chop(l):
    del l[0]
    del l[-1]   #deletes first index from end of list (last element)
    return None
#permanently modifies old list; now l no longer has its former 1st and last elements

def middle(l):
    return l[1:-1]  #returns second to second-last value
#does not modify old list, just returns new one that's a section of it

l = [1, 2, 3, 4, 5]

newlist = middle(l)
print(newlist)

chop(l)   #have to do this one after calling middle because permanently mods l
print(l)        


