score = input("Enter score: ")

try :
    score = float(score)

except :
    print("Bad score")
    quit()

def computegrade(score) :
    if score < 0.0 or score > 1.0 :
        print("Bad score")

    elif score >= 0.9 :
        print("A")
    
    elif score >= 0.8 :
        print("B")

    elif score >= 0.7 :
        print("C")

    elif score >= 0.6 :
        print("D")

    elif score < 0.6 :
        print("F")

computegrade(score)      #call line

#after running this program (def is established), can do things like
# >>> computegrade(0.9) and have it properly spit out A!
