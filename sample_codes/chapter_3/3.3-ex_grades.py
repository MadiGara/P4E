score = input("Enter score between 0.0 and 1.0: ")

try :
    score = float(score)
    print("Enter score:", score)

except :
    print("Enter score:", score)
    print("Bad score")
    quit()

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

