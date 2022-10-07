# word counter program 

mydic={'h':'2', 'h':'334'}

print(mydic)

def wordCounter(s):
    count={}
    for char in s:
        count[char]=char.count(s)
    return count

print(wordCounter('abubakare'))
