string = 'banana'
letter = 'a'
# could take out top two lines and put in input statements
# but function itself works like this and code is as asked in q

def count(string, letter):
    count = 0
    for place in string:
        if place == letter:
            count = count + 1
    print(count)

total_count = count(string, letter)
