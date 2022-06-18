str = 'X-DSPAM-Confidence:0.8475'
start = str.find(':')
number = str[start+1:]
number = float(number)
print(number)
