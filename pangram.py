import string
def is_pangram(s):
    a=set(string.lowercase)
    b=set(s.lowe())

    return a.issubset(b)

u=input("Enter your sentence")

if is_pangram(u):
    print("correct")

else:
    print("incorrect")

