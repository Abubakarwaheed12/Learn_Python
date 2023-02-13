# word counter program 

# mydic={'h':'2', 'h':'334'}

# print(mydic)

def wordCounter(s):
    count1={}
    for char in s:
        if char==char:
            c=s.count(char)
            count1[char]=c
    return count1

print(wordCounter('hhh nn nn '))
